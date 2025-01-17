import os

import streamlit as st
from llm_in_production.openai_utils import get_openai_client

PAGE_TILE = "Custom LLM App"
st.set_page_config(page_title=PAGE_TILE, page_icon="📊")
st.title(PAGE_TILE)


client = get_openai_client()

with st.sidebar:
    st.header("Settings")
    st.write("Whatever your application needs")

    clear_chat_history = st.button("clear chat history")
    if clear_chat_history:
        st.session_state.messages = []


st.write("The sky is the limit!")

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

    message_placeholder = st.empty()

    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant that helps people with their daily tasks.",
        }
    ]
    for m in st.session_state.messages:
        messages.append({"role": m["role"], "content": m["content"]})

    response = client.chat.completions.create(
        model=os.environ["GPT_4_MODEL_NAME"],
        messages=messages,
    )
    assistant_message = response.choices[0].message.content
    message_placeholder.markdown(assistant_message)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )
