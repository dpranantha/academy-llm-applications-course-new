import dotenv

import streamlit as st
from llm_in_production.llm import instantiate_langchain_model

dotenv.load_dotenv()


# Here we create the client.
# Make sure you select the LLM provider that corresponds to the one you are using in this course!
client = instantiate_langchain_model(
    llm_provider="azure",
    # llm_provider="gcp",
)

PAGE_TILE = "Summarizer App"
st.set_page_config(page_title=PAGE_TILE, page_icon="📊")
st.title(PAGE_TILE)


with st.sidebar:
    st.header("Settings")
    # Exercise: add settings for
    #   - max_tokens
    #   - temperature
    #   - top_p
    #   - Bonus the number of sentences to summarize to
    # YOUR CODE HERE START
    max_tokens = st.number_input(
        "Max tokens", min_value=1, value=1024, step=1, max_value=2048
    )
    temperature = st.slider(
        "Temperature", min_value=0.0, value=1.0, step=0.1, max_value=1.0
    )
    top_p = st.slider("Top p", min_value=0.0, value=1.0, step=0.1, max_value=1.0)
    num_sentences = st.number_input(
        "Number of sentences", min_value=1, value=1, step=1, max_value=5
    )
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
            {
                "role": "system",
                "content": "You task is to summarize the most important information "
                + f"of the text the user provides you in at most {num_sentences} sentences.",
            },
            # YOUR CODE HERE END
            {"role": "user", "content": prompt},
        ]

        response = client.invoke(
            input=messages,
            # Exercise: add max_tokens, temperature and top_p to the completion request
            # YOUR CODE HERE START: test 123
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            # YOUR CODE HERE END
        )
        message = response.content
        message_placeholder.markdown(message)
