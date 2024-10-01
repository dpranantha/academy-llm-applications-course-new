import os

import dotenv

import streamlit as st
from llm_in_production.openai_utils import get_openai_client

PAGE_TILE = "SummarizerGPT"
st.set_page_config(page_title=PAGE_TILE, page_icon="📊")
st.title(PAGE_TILE)


dotenv.load_dotenv()
client = get_openai_client()

with st.sidebar:
    st.header("Settings")
    # Exercise: add settings for
    #   - max_tokens
    #   - temperature
    #   - top_p
    #   - Bonus the number of sentences to summarize to
    # YOUR CODE HERE START
    # YOUR CODE HERE END


# Accept user input
prompt = st.chat_input("Add your text here")

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        messages = [
            # Exercise: Add a system message that describes the assistant's task.
            # Bonus: make the prompt configurable from the sidebar
            # YOUR CODE HERE START
            # YOUR CODE HERE END
            {"role": "user", "content": prompt},
        ]

        response = client.chat.completions.create(
            model=os.environ["GPT_35_CHAT_MODEL_NAME"],
            messages=messages,
            # Exercise: add max_tokens, temperature and top_p to the completion request
            # YOUR CODE HERE START: test 123
            # YOUR CODE HERE END
        )
        message = response.choices[0].message.content
        message_placeholder.markdown(message)