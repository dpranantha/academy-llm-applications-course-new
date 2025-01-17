import json
import os
from pathlib import Path

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import streamlit as st
from llm_in_production.huggingface_utils import get_device
from llm_in_production.openai_utils import (
    get_number_of_tokens,
    get_openai_client,
    pop_message_untill_less_tokens_then,
)

title = "PyData Amsterdam 2023 Q&A bot"
st.set_page_config(
    page_title=title,
    page_icon="👋",
    layout="wide",
)
st.title(title)

MAX_TOKENS = 4096

client = get_openai_client()

# Here we load in the PyData Amsterdam 2023 data.
with open(Path(__file__).parent / "../pydata.json", "r") as f:
    pydata_data = json.load(f)
    talks = pydata_data["talks"]


def build_db(chunk_size: int, chunk_overlap: int):
    """
    Build the vector store that will be used to search through the talks.
    :param chunk_size: The max number of tokens per chunk.
    :param chunk_overlap: The number of overlapping tokens between chunks.
    :return: A vector database.
    """

    # Here we create the embedding function that will be used to embed the sentences.
    embedding_func = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2", model_kwargs={"device": get_device()}
    )

    # Here we create the text splitter that will be used to split the talks into chunks.
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        separators=[
            "\n\n",
            "\n",
            ".",
            "?",
            "!",
            " ",
            "",
        ],  # Feel free to add more separators.
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=get_number_of_tokens,
        keep_separator=True,  # Feel free to change this.
        strip_whitespace=True,  # Feel free to change this.
    )

    # Here we collect the text chunks and their metadata.
    texts = []
    metadatas = []
    for talk in talks:
        title = talk["title"]
        speakers = ", ".join(talk["speakers"])
        talk_type = talk["type"]
        duration = talk["duration"]
        date = talk["date"]
        room = talk["room"]
        # Here we create the metadata for the talk. This is the same for every chunk of the talk.
        metadata = {
            "title": title,
            # Add additional metadata about the talk such as the talk type, speakers, date, room and duration
            # YOUR CODE HERE START
            "type": talk_type,
            "speakers": speakers,
            "duration": duration,
            "date": date,
            "room": room
            # YOUR CODE HERE END
        }

        texts.append(f"Title: {title}")
        metadatas.append(metadata)

        texts.append(f"Speakers: {speakers}")
        metadatas.append(metadata)

        # YOUR CODE HERE START: Chunk the talk description and abstract and add them to the texts and metadatas lists.
        abstract = talk["abstract"]
        for chunk in text_splitter.split_text(abstract):
            texts.append(chunk)
            metadatas.append(metadata)
        description = talk["description"]
        for chunk in text_splitter.split_text(description):
            texts.append(chunk)
            metadatas.append(metadata)
        # YOUR CODE HERE END

    # Here we create the vector database.
    return FAISS.from_texts(texts, metadatas=metadatas, embedding=embedding_func)


def format_search_result(document, idx: int) -> str:
    """
    The formats a search result.
    :param document: The document that needs to be formatted.
    :param idx: Number indicating the order of the document in the search results (lower is better).
    :return: A formatted string that contains all the information about the document that is relevant for the LLM.
    """

    # Extract the title and document.
    title = document.metadata["title"]
    page_content = document.page_content

    # Start the string that contains all the information about the document that is relevant for the LLM.
    # with a number indicating the order of the document in the search results.
    combined_search_results = f"Result {idx}:\n"
    # Give the LLM access to additional information about the talk
    # such as the title, talk type, speakers, date, room and duration.
    # YOUR CODE HERE START:
    combined_search_results += f"Title: {title}\n"
    combined_search_results += f"Talk type: {document.metadata['type']}\n"
    combined_search_results += f"Speakers: {document.metadata['speakers']}\n"
    combined_search_results += (
        f"When: {document.metadata['date']} at {document.metadata['room']}\n"
    )
    combined_search_results += f"Duration: {document.metadata['duration']}\n"
    combined_search_results += f"Excerpt: {page_content}\n"
    # YOUR CODE HERE END

    return combined_search_results.strip()


def format_search_instruction(user_query: str, documents) -> str:
    """
    This formats the search instruction prompt to the LLM.
    :param user_query: The query that the user has entered.
    :param documents: The documents that are returned by the search.
    :return: The formatted search instruction prompt for the LLM.
    """
    search_results = "\n\n".join(
        format_search_result(document, idx + 1)
        for idx, document in enumerate(documents)
    ).strip()
    # TODO: improve this prompt to your liking.
    return f"""
    For a given query, you have searched through the talk descriptions of PyData Amsterdam 2023.
    The top {len(documents)} results are shown below.

    Formulate an answer to the query using only the relevant source(s).
    Link to the source(s) by mentioning the talk title.

    SEARCH RESULTS:
    {search_results}

    SEARCH QUERY:
    {user_query}

    State your reply to this query concisely, based on the search results you've found.
    """.strip()


with st.sidebar:
    st.header("General settings")
    max_tokens = st.number_input(
        "Max tokens", min_value=1, value=256, step=1, max_value=1024
    )
    # YOUR CODE HERE START: Add the settings for temperature and top_p
    temperature = st.slider(
        "Temperature", min_value=0.0, value=1.0, step=0.1, max_value=1.0
    )
    top_p = st.slider("Top p", min_value=0.0, value=1.0, step=0.1, max_value=1.0)
    # YOUR CODE HERE END

    n_search_results = st.number_input(
        "Number of search results", min_value=0, value=3, step=1, max_value=6
    )

    st.header("Vector database settings")
    st.markdown("Changing these settings require a reindexing of the database.")
    # Exercise: add settings for max_tokens, temperature and top_p
    chunk_size = st.number_input(
        "Max number of tokens per chunk", min_value=1, value=150, step=1, max_value=256
    )
    chunk_overlap = st.number_input(
        "Number of overlapping tokens",
        min_value=0,
        value=int(chunk_size * 0.1),
        step=1,
        max_value=chunk_size // 2,
    )

    def on_reindex():
        """Start the reindexing process of the vector database."""
        if "db" in st.session_state:
            # Delete the old database
            del st.session_state["db"]

        # Store a new database
        st.session_state["db"] = build_db(
            chunk_size=chunk_size, chunk_overlap=chunk_overlap
        )

    submit = st.button("Re-index", on_click=on_reindex)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "db" not in st.session_state:
    st.session_state["db"] = build_db(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )


#    Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        content = message["content"]
        if message["role"] == "user":
            st.text(content)
        else:
            st.markdown(content.replace("\n", "\n\n"))
# Search through the talks
search_talks = st.checkbox("Search through the talks when answering questions")
# Accept user input
prompt = st.chat_input(
    "What is your question about PyData Amsterdam 2023? (Click the checkbox to search through the talk descriptions)"
)
if prompt:
    # Check if the user wants to search through the talks
    if search_talks:
        # Search through the talks
        db = st.session_state.db
        documents = db.similarity_search(prompt, k=n_search_results)
        # Change the prompt to the result of the search
        prompt = format_search_instruction(prompt, documents)

    # Add user message to chat history
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.text(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()

        messages = [
            # Add a system message that describes the bot and general information about PyData Amsterdam 2023
            # such as the start and end date and the rooms.
            # YOUR CODE HERE START
            {
                "role": "system",
                "content": "You are a Q&A bot for PyData Amsterdam 2023. "
                + f"It starts on {pydata_data['start_date']} "
                f"and ends on {pydata_data['end_date']}. "
                f"The rooms have the following names and capacities: {pydata_data['rooms']}.",
            },
            # YOUR CODE HERE END
        ]
        # Add all the messages from the chat history to the messages list
        for m in st.session_state.messages:
            messages.append({"role": m["role"], "content": m["content"]})

        # Ensures that the text fits into the token limit of the model by removing the oldest messages
        messages = pop_message_untill_less_tokens_then(
            messages, MAX_TOKENS - max_tokens
        )

        response = client.chat.completions.create(
            model=os.environ["GPT_35_CHAT_MODEL_NAME"],
            messages=messages,
            max_tokens=max_tokens,
            # YOUR CODE HERE START: Add the settings for temperature and top_p
            temperature=temperature,
            top_p=top_p,
            # YOUR CODE HERE END
        )
        assistant_message = response.choices[0].message.content
        # Display assistant message in chat message container
        message_placeholder.markdown(assistant_message)

    # Add assistant message to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_message}
    )
