import inspect
import json
import logging
import re
from typing import Any, Callable, Dict

from langchain_core.utils.function_calling import convert_to_openai_function

# Suppress HTTPX request logs
logging.getLogger("httpx").setLevel(logging.WARNING)

# Suppress Gemini multiple function call warning
logging.getLogger("langchain_google_vertexai.chat_models").setLevel(logging.ERROR)

# Suppress LangChain verbose logs (optional)
logging.getLogger("langchain").setLevel(logging.WARNING)


def execute_tool(
    tool_name: str, tool_args: Dict[str, Any], available_tools: Dict[str, Callable]
) -> str:
    """Executes a tool and returns the response as a JSON string."""
    if tool_name not in available_tools:
        error_message = {
            "error": f"Tool '{tool_name}' not found. Available tools: {list(available_tools.keys())}"
        }
        logging.error(error_message["error"])
        return json.dumps(error_message)

    try:
        return json.dumps(available_tools[tool_name](**tool_args))
    except Exception as e:
        logging.error(f"Error executing tool '{tool_name}': {e}")
        return json.dumps({"error": str(e)})


def tool_calling_agent(
    client,
    system_prompt: str,
    user_prompt: str,
    *tools: Callable,
    react: bool = False,
    temperature: float = 0.0,
    iterations: int = 3,
    seed: int = 0,
) -> str:
    """Generates a response using AI and invokes available tools if necessary."""

    tool_definitions = [
        {"type": "function", "function": convert_to_openai_function(tool)}
        for tool in tools
    ]
    available_tools = {tool.__name__: tool for tool in tools}

    if react:
        system_prompt += get_react_prompt(tools)  # Use updated ReAct prompt

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    output_logs = []

    for i in range(iterations):
        # Step 1: AI Generates a Thought or an Action
        response = client.invoke(
            input=messages, tools=tool_definitions, seed=seed, temperature=temperature
        )
        messages.append(response)
        output_logs.append(f"\n### Model Output:\n\n{response.content}\n")

        # Check if the model reached a final answer
        if "Final Answer:" in response.content:
            break  # Stop iterating if the model has concluded

        # Step 2: Check if an Action (tool call) is required
        tool_calls = response.tool_calls
        if not tool_calls:
            break  # No tools needed, exit loop

        tool_responses = []
        for tool_call in tool_calls:
            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            # Step 3: Execute the tool and capture response
            tool_response = execute_tool(tool_name, tool_args, available_tools)

            # Log tool execution
            output_logs.append(
                f"\n### Tool Called: {tool_name} with args: {tool_args}\n"
            )

            # Step 4: Append the Observation response
            tool_responses.append(
                {
                    "role": "assistant",  # Keep it within the ReAct format
                    "content": f"Observation: {tool_response}",
                }
            )

        messages.extend(tool_responses)

    else:
        output_logs.append(
            "\n### Maximum iterations reached. Stopping further tool calls.\n"
        )

    return "".join(output_logs)


def get_react_prompt(tools):
    """Generates a ReAct-style prompt for decision-making."""
    tool_names = [tool.__name__ for tool in tools]

    return f"""
Answer the following questions as best you can.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, could be one of the given tools: {tool_names}
At this point you may call for an action to be taken, but you must return the Question and Thought as content in your response
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!
"""


def type_mapping(dtype):
    """Map Python data types to a JSON equivalent."""
    return {
        float: "number",
        int: "integer",
        str: "string",
    }.get(dtype, "object")


def extract_params(doc_str: str):
    """Extract parameter information from a docstring (reST-style)."""
    params = {}
    for line in doc_str.split("\n"):
        line = line.strip()
        if line.startswith(":param"):
            param_match = re.search(r":param (\w+): (.+)", line)
            if param_match:
                params[param_match.group(1)] = param_match.group(2)
    return params


def function_to_json(func):
    """Convert a Python function into the JSON format expected by the model."""
    argspec = inspect.getfullargspec(func)
    function_doc = inspect.getdoc(func) or ""

    param_details = extract_params(function_doc)
    params = {
        param: {
            "description": param_details.get(param, ""),
            "type": type_mapping(argspec.annotations.get(param, type(None))),
        }
        for param in argspec.args
    }

    optional_params = argspec.defaults or ()
    return {
        "name": func.__name__,
        "description": function_doc.split("\n", 1)[0],  # First line of docstring
        "parameters": {"type": "object", "properties": params},
        "required": [arg for arg in argspec.args if arg not in optional_params],
    }
