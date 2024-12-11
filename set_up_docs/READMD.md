# Docs for trainers

This folder contains information for setting up with OpenAI on Azure.


- [ ] Create a new Azure OpenAI services resource on the [Azure portal](https://portal.azure.com/#home).
- [ ] Deploy the following models to the Azure OpenAI services resource ([how to](how-to-deploy-aoi-models.md)):
    - [ ] The chat model: `gpt-4o-mini`.
    - [ ] The chat model: `gpt-35-turbo`.
    - [ ] The text completion model: `gpt-35-turbo-instruct`.
    - [ ] The text completion base model: `babbage-002`.
- [ ] I have validated the models have a reasonable quota ([how to](How-to-ensure-each-model-deployment-has-enough-quotas.md)).
- [ ] Obtain the following environment variables and added them as GitHub CodeSpaces secrets ([how to](how-to-set-github-codespace-secrets.md)):
    - [ ] `OPENAI_API_KEY`: The API key of your Azure OpenAI services resource (see [how to](how-to-obtain-openai-api-keys.md)).
    - [ ] `OPENAI_API_BASE`: The base URL of your Azure OpenAI services resource, i.e the Endpoint, e.g. `https://<your_oai_services_name>.openai.azure.com/`.
    - [ ] `OPENAI_API_TYPE`: `azure`. (If for some reason you are using a different provider, you can change this.)
    - [ ] `GPT_35_TURBO_INSTRUCT_MODEL_NAME`: The deployment name of your `gpt-35-turbo-instruct` model.
    - [ ] `GPT_35_CHAT_MODEL_NAME`: The deployment name of your `gpt-35-turbo` model.
    - [ ] `BABBAGE_MODEL_NAME`: The deployment name of your `babbage-002` model.
    - [ ] `WEATHER_API_KEY`: The key for the weather API used in `04_agents`. A key can be attained from https://www.weatherapi.com on the [free plan](https://www.weatherapi.com/pricing.aspx).
    - [ ] `NEWS_API_KEY`: The key for the news API used in `04_agents`. A key can be attained from https://www.newsapi.com on the [free plan](https://newsapi.org/pricing).
- [ ] Remember to reset the Azure OpenAI API key regularly to prevent abuse ([how to](how-to-reset-openai-api-keys.md)).

