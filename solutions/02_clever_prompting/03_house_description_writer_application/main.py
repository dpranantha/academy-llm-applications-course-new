import json
from typing import Any

import pydantic

import streamlit as st
from llm_in_production.llm import instantiate_langchain_model
from llm_in_production.text_extraction import (
    BooleanFeature,
    DigitFeature,
    StringFeature,
)

HOUSE_TYPES = ["Apartment", "House", "Studio"]

# Here we create the client.
# Make sure you select the LLM provider that corresponds to the one you are using in this course!
client = instantiate_langchain_model(
    llm_provider="azure",
    # llm_provider="gcp",
)


####################
# Logic for the UI #
####################


class HouseFeatures(pydantic.BaseModel):
    """Correctly extracted house listing features"""

    house_type: StringFeature = pydantic.Field(
        description=f"Must be one of the following: {', '.join(HOUSE_TYPES)}"
    )
    rent: DigitFeature
    city: StringFeature
    # YOUR CODE HERE START: Add the other features like neighborhood, animals_allowed, number_of_bedrooms and others you can think of
    neighborhood: StringFeature
    pets_allowed: BooleanFeature
    number_of_bedrooms: DigitFeature
    # YOUR CODE HERE END


def generate_description(data: dict[str, Any]) -> str:
    """
    Generate a text description of a house based on the data provided by the user.
    :param data: A dictionary where the keys are the feature names and the values are the feature values
    :return: A text description of the house
    """

    # YOUR CODE HERE START: Write a system prompt that explains the task to the model
    system_prompt = "Your tast is to write a single house descriptions for a real estate website based on the information the user provides"
    # YOUR CODE HERE END

    messages = [
        # YOUR CODE HERE START: Add the system prompt if needed
        {"role": "system", "content": system_prompt},
        # YOUR CODE HERE END
        {"role": "user", "content": json.dumps(data)},
    ]

    response = client.invoke(
        input=messages,
        temperature=1.0,
    )

    message = response.content
    return message


def extract_features(description: str) -> HouseFeatures | None:
    """
    Extract the features from a description of a house in the HouseFeatures schema.
    :param description:
    :return:
    """
    # YOUR CODE HERE START: Replace this your system prompt.
    # Note, if using GPT, you no longer need to pass the schema as part of the sytem prompt,
    # this can now be done in the `response_format` parameter of the `client.invoke` method.
    system_prompt = """
    You are tasked with extracting structured information from a user's description of a house.
    For each feature (e.g., pets_allowed, neighborhood, number_of_bedrooms, city, etc.):
    - Extract details explicitly mentioned or reasonably inferred from the description.
    - Provide the following fields for each feature:
        1. `thoughts`: A brief explanation of how you arrived at the value based on your observations. If inferred, explain the reasoning.
        2. `quotes`: The exact sentences or fragments from the description that support your conclusion.
            This can include indirect evidence for inferred values.
        3. `value`: The value explicitly quoted in the description or inferred from context. If no relevant information is present, return `None`.

    Inference is allowed **only if the context is clear and your reasoning is explicitly explained**.
    Strictly adhere to this format and return a structured JSON response.
    """.strip()
    # YOUR CODE HERE END

    messages = [
        # YOUR CODE HERE START: Add the system prompt if needed
        {"role": "system", "content": system_prompt},
        # YOUR CODE HERE END
        {"role": "user", "content": description},
    ]

    # Invoke the LLM
    response = client.invoke(
        input=messages,
        # Select the correct parameter based on the LLM provider you are using
        response_format=HouseFeatures,  # OpenAI or Azure
        temperature=0.0,
    )

    message = response.content
    house_features = HouseFeatures.model_validate_json(message)
    return house_features

    # # You may want to include a check that the response matches the specific JSON schema
    # # If the response does not match the schema, you can ask the LLM to correct the response
    # try:
    #     house_features = HouseFeatures.model_validate_json(message)
    # except pydantic.ValidationError as e:
    #     st.error("Attempting to correct initial generation...", icon="🚨")
    #     # Tell the LLM to fix the validation errors by:
    #     # 1. Adding its response to the messages
    #     # 2. Adding a user message explaining that the response did not correspond to the JSON schema and what the errors are
    #     # 3. Sending all the messages to the LLM again
    #     # 4. Extracting the features from the corrected response

    #     # YOUR CODE HERE START:
    #     messages.append({"role": "assistant", "content": message})

    #     messages.append(
    #         {
    #             "role": "user",
    #             "content": f"Your response is incorrect! Respond only with JSON that does not have these errors: {e.errors()}",
    #         }
    #     )

    #     response = client.invoke(
    #         input=messages,
    #         # Select the correct parameter based on the LLM provider you are using
    #         response_format=HouseFeatures, # OpenAI or Azure
    #         temperature=0.0,
    #     )

    #     message = response.content
    #     house_features = HouseFeatures.model_validate_json(message)
    #     # YOUR CODE HERE END

    # return house_features


def on_click_generate(data: dict[str, Any]):
    """
    This function is called when the user clicks the "Generate" button.
    It generates a description and extracts the features from it for validation.
    :param data: This is dict with the user input values. E.g. `{"rent": 1000, "city": "Amsterdam", ...}`.
    :return: None
    """

    # Here we generate the description based on the user input
    description = generate_description(data)

    # Here we extract the features from the description such that we can check description is correct
    features_in_description = extract_features(description)

    # Here we store the description and the extracted features in the session state
    # This tells Streamlit to remember these values and to re-render the UI
    st.session_state["description"] = description
    st.session_state["features"] = features_in_description


######################
# Start Streamlit UI #
######################

title = "House description writer"
st.set_page_config(
    page_title=title,
    page_icon="👋",
    layout="wide",
)
st.title(title)


# This is the sidebar where we collect the user input
with st.sidebar:
    st.title("Settings")

    city = st.text_input("In which city is it located?", value="Amsterdam")
    rent = st.number_input("How much is the rent?", min_value=0, step=50, value=1000)
    house_type = st.selectbox("Select a house type", options=HOUSE_TYPES, index=0)

    # YOUR CODE HERE START: Add the other features like neighborhood, animals_allowed, number_of_bedrooms and others you can think of
    neighborhood = st.text_input(
        "In which neighborhood is it located?", value="Oud-West"
    )
    pets_allowed = st.checkbox("Are pets allowed?", value=False)
    number_of_bedrooms = st.number_input(
        "How many bedrooms does it have?", min_value=1, value=1, step=1
    )
    # YOUR CODE HERE END

    # Here we collect the user input values
    data = {
        "rent": rent,
        "city": city,
        # YOUR CODE HERE START: Add the other features like house_type, neighborhood, animals_allowed, number_of_bedrooms
        "house_type": house_type,
        "neighborhood": neighborhood,
        "animals_allowed": pets_allowed,
        "number_of_bedrooms": number_of_bedrooms,
        # YOUR CODE HERE END
    }

    # Pressing this button will trigger the on_click_generate function defined above
    # This will generate a description and extract the features
    submit = st.button("Generate", on_click=lambda: on_click_generate(data))


# Here we create two columns to render the description and the extracted features side by side
col1, col2 = st.columns(2)


# This is the left column where we render the generated description
with col1:
    is_there_a_description = "description" in st.session_state
    if is_there_a_description:
        st.write(st.session_state["description"])
    else:
        st.write("No description yet")


def render_feature(
    name: str, qoutes: list[str] | None, value: Any | None, expected_value: Any
):
    """This a utility function to render a feature in the UI"""

    st.write(f"### {name}")
    if value is None:
        st.write(f"Missing value for {name}")
    else:
        st.write(f"Value: {value}")
        is_correct = value == expected_value
        # YOUR CODE HERE START: Show if the generated value is correct
        if is_correct:
            st.write("✅ Correct")
        else:
            st.write("❌ Incorrect")
            st.write(f"Expected value: {expected_value}")
        # YOUR CODE HERE END

    if qoutes is not None:
        st.write("Quotes:")
        for quote in qoutes:
            st.write(f"- {quote}")


# This is the right column where we render the extracted features
with col2:
    if "features" in st.session_state:
        features = st.session_state["features"]
        if features is None:
            st.write("Features could not be extracted.")
        else:
            render_feature(
                "City",
                features.city.quotes,
                features.city.value,
                expected_value=city,
            )
            render_feature(
                "Rent",
                features.rent.quotes,
                features.rent.value,
                expected_value=rent,
            )
            # YOUR CODE HERE START: Render the other features
            render_feature(
                "Neighborhood",
                features.neighborhood.quotes,
                features.neighborhood.value,
                expected_value=neighborhood,
            )
            render_feature(
                "House type",
                features.house_type.quotes,
                features.house_type.value,
                expected_value=house_type,
            )
            render_feature(
                "Pets allowed",
                features.pets_allowed.quotes,
                features.pets_allowed.value,
                expected_value=pets_allowed,
            )
            render_feature(
                "Number of bedrooms",
                features.number_of_bedrooms.quotes,
                features.number_of_bedrooms.value,
                expected_value=number_of_bedrooms,
            )
            # YOUR CODE HERE END

    else:
        st.write("No features yet")
