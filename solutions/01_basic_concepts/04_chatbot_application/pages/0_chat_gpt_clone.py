import os

import streamlit as st
from llm_in_production.openai_utils import get_openai_client

title = "Chatbot App"
st.set_page_config(
    page_title=title,
    page_icon="👋",
)
st.title(title)


client = get_openai_client()

with st.sidebar:
    st.header("Settings")
    # Exercise: add settings for max_tokens, temperature and top_p
    # YOUR CODE HERE START
    max_tokens = st.number_input(
        "Max tokens", min_value=1, value=1024, step=1, max_value=2048
    )
    temperature = st.slider(
        "Temperature", min_value=0.0, value=1.0, step=0.1, max_value=1.0
    )
    top_p = st.slider("Top p", min_value=0.0, value=1.0, step=0.1, max_value=1.0)
    # YOUR CODE HERE END


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input("What is up?")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        messages = [
            # Exercise: Add a system message that describes the assistant's task.
            # Bonus: make the prompt configurable from the sidebar
            # YOUR CODE HERE START
            {
                "role": "system",
                "content": "You are an AI assistant that helps people with their daily tasks.",
            }
            # YOUR CODE HERE END
        ]
        for m in st.session_state.messages:
            messages.append({"role": m["role"], "content": m["content"]})

        response = client.chat.completions.create(
            model=os.environ["GPT_4_MODEL_NAME"],
            messages=messages,
            # Exercise: add max_tokens, temperature and top_p to the completion request
            # YOUR CODE HERE START: test 123
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            # YOUR CODE HERE END
        )
        assistant_message = response.choices[0].message.content
        message_placeholder.markdown(assistant_message)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )
