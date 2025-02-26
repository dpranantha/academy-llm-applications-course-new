# %%writefile simple_chatbot.py

import streamlit as st
from llm_in_production.llm import instantiate_langchain_model
import dotenv

# Step 1: Set up Streamlit UI
title = "Simple Chatbot"
st.set_page_config(
    page_title=title,
    page_icon="👋",
)
st.title(title)

# Step 2: Create LLM Client
dotenv.load_dotenv()

# Here we create the client. 
# Make sure you select the LLM provider that corresponds to the one you are using in this course!
client = instantiate_langchain_model(
    # llm_provider="azure",
    llm_provider="gcp",
)
st.write("Powered by", client.model_name)


# Step 3: Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Step 4: Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Step 5: Accept User Input
prompt = st.chat_input("Say something:")

if prompt:
    # Add user message to chat history
    input_message = {"role": "user", "content": prompt}
    st.session_state.messages.append(input_message)

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simple response logic
    response_message = client.invoke(st.session_state.messages).content
    
    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(response_message)
    
    # Store assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response_message}
    )