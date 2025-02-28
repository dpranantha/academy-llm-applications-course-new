import os
from typing import Literal

from dotenv import load_dotenv
from langchain_core.language_models.chat_models import BaseChatModel


def instantiate_langchain_model(
    llm_provider: Literal["gcp", "azure", "aws", "openai"] | None = None
) -> BaseChatModel:
    if llm_provider is None:
        load_dotenv()
        llm_provider = os.environ["LLM_PROVIDER"]

    match llm_provider:
        case "gcp":
            from langchain_google_vertexai.chat_models import ChatVertexAI

            return ChatVertexAI(
                model="gemini-1.5-flash",
                project=os.getenv("GCP_PROJECT_ID"),
                location=os.getenv("GCP_LOCATION"),
            )

        case "azure":
            from langchain_openai import AzureChatOpenAI

            # replace the openai environment variables with the azure ones
            # otherwise the azure client will not work
            if "OPENAI_API_BASE" in os.environ.keys():
                os.environ["AZURE_OPENAI_ENDPOINT"] = os.environ["OPENAI_API_BASE"]
                del os.environ["OPENAI_API_BASE"]
            if "OPENAI_API_KEY" in os.environ.keys():
                os.environ["AZURE_OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]
                del os.environ["OPENAI_API_KEY"]

            return AzureChatOpenAI(
                api_version="2025-01-01-preview",
                azure_deployment=os.environ["GPT_4_MODEL_NAME"],
                model_name=os.environ["GPT_4_MODEL_NAME"],
            )

        case "openai":
            from langchain_openai import ChatOpenAI

            return ChatOpenAI(
                api_key=os.environ["OPENAI_API_KEY"],
                model_name=os.environ["GPT_4_MODEL_NAME"],
            )

        case _:
            raise ValueError(f"Unknown LLM provider: {llm_provider}")
