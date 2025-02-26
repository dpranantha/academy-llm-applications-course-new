import copy

from langchain.schema import BaseMessage


def pop_messages_until_within_token_limit(
    messages: list[BaseMessage], token_limit: int, client
) -> list[BaseMessage]:
    """
    Ensure that the messages fit within the token limit for the model by
    progressively removing the earliest messages.
    """
    messages = copy.deepcopy(messages)

    while get_n_tokens_in_messages(messages, client) > token_limit:
        messages.pop(0)

    return messages


def get_n_tokens_in_messages(messages: list[BaseMessage], client) -> int:
    """
    Get the total number of tokens in a list of messages.
    This function supports LangChain message objects.
    """
    all_text = " ".join(message["content"] for message in messages)
    return client.get_num_tokens(all_text)
