import os

import dotenv
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent

import streamlit as st
from llm_in_production.openai_utils import get_openai_client

dotenv.load_dotenv()


# Set the page title
# YOUR CODE HERE START
st.set_page_config(page_title="🦜🔗 Talk to the Data Chatbot")
st.title("Talk to the Data with 🦜🔗")
# YOUR CODE HERE END


# Load CSV file
def load_csv(input_csv):
    df = pd.read_csv(input_csv)
    # Add the option to visualize the uploaded data
    # YOUR CODE HERE START
    with st.expander("Visualize uploaded data"):
        st.write(df)
    # YOUR CODE HERE END
    return df


# Generate LLM response
def generate_response(client, df, input_query):
    # Create Pandas DataFrame Agent
    agent = create_pandas_dataframe_agent(
        client,
        df,
        # Pass additional arguments to enable the model to
        # return the intermediate steps it took and
        # allow for enhanced verbosity and error handling.
        # YOUR CODE HERE START
        verbose=True,
        return_intermediate_steps=True,
        agent_executor_kwargs={"handle_parsing_errors": True}
        # YOUR CODE HERE END
    )
    # Perform Query using the Agent
    response = agent.invoke(input_query)
    return response


# Suggested questions
question_list = [
    "How many rows are there?",
    # YOUR CODE HERE START
    "What is the max value for the weight column?",
    "How many different diets are there?",
    "What is the max value of the weight column? Is it bigger than the max value of the time column?",
    "Other"
    # YOUR CODE HERE END
]


# Here we read in the data
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = load_csv(uploaded_file)

    query_text = st.selectbox(
        "Select an example query:",
        question_list,
        index=None,
        placeholder="select an option",
        disabled=not uploaded_file,
    )

    # Add an option for users to enter their own queries
    # YOUR CODE HERE START
    if query_text == "Other":
        query_text = st.text_input(
            "Enter your query:",
            placeholder="Enter query here ...",
            disabled=not uploaded_file,
        )
    # YOUR CODE HERE END

    if query_text:
        st.header("Output")
        # get client
        client = get_openai_client(
            use_langchain=True,
            model_name=os.environ["GPT_35_CHAT_MODEL_NAME"],
            temperature=0,
        )
        # get response
        response = generate_response(client, df, query_text)
        st.success(response["output"])

        # Add an option for users to see the intermediate steps taken by the model
        # YOUR CODE HERE START
        with st.expander("See thought process"):
            for step in response["intermediate_steps"]:
                st.write(step[0].log)
        # YOUR CODE HERE END
