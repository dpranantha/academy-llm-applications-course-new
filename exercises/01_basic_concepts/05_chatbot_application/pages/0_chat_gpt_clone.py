import dotenv

import streamlit as st
from llm_in_production.llm import instantiate_langchain_model

dotenv.load_dotenv()


# Here we create the client.
# Make sure you select the LLM provider that corresponds to the one you are using in this course!
client = instantiate_langchain_model(
    # llm_provider="azure",
    llm_provider="gcp",
)

title = "Chatbot App"
st.set_page_config(
    page_title=title,
    page_icon="👋",
)
st.title(title)


with st.sidebar:
    st.header("Settings")
    # Exercise: add settings for max_tokens, temperature and top_p
    # YOUR CODE HERE START
    st.sidebar.markdown("# Controls")
    max_tokens = st.sidebar.slider("Max Tokens", min_value=0, max_value=1000, value=1000)
    temperature = st.sidebar.slider("Temperature", min_value=0.01, max_value=2.0, value=1.0, step=0.1)
    top_p = st.sidebar.slider("Top-p", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    system_prompt = st.sidebar.text_input(label="System Prompt", value="You are a helpful assistant that help with every day task!")
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
            system_prompt
            # YOUR CODE HERE END,
        ]
        for m in st.session_state.messages:
            messages.append({"role": m["role"], "content": m["content"]})

        response = client.invoke(
            input=messages,
            # Exercise: add max_tokens, temperature and top_p to the completion request
            # YOUR CODE HERE START: test 123
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
            # YOUR CODE HERE END
        )
        assistant_message = response.content
        message_placeholder.markdown(assistant_message)

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )