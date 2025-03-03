# Azure OpenAI

## Checklist for the training
Bellow you find a checklist that helps you to prepare for the training.
Make you don't forget anything by checking off the items on the list.
It also contains links to the relevant how-to guides if you need more information.

### Before the training
- [ ] I have created a new Azure OpenAI services resource for this training ([how to](how-to-deploy-aoi-infrastructure.md)).
- [ ] I have deployed the following models to the Azure OpenAI services resource ([how to](how-to-deploy-aoi-models.md)):
    - [ ] The chat model: `gpt-35-turbo`.
    - [ ] The text completion model: `gpt-35-turbo-instruct`.
    - [ ] GPT 4o mini: `gpt-4o-mini`.
- [ ] I have validated the models have a reasonable quota ([how to](How-to-ensure-each-model-deployment-has-enough-quotas.md)).
- [ ] I obtained the following environment variables and added them as GitHub CodeSpaces secrets ([how to](how-to-set-github-codespace-secrets.md)):
    - [ ] `OPENAI_API_KEY`: The API key of your Azure OpenAI services resource (see [how to](how-to-obtain-openai-api-keys.md)).
    - [ ] `OPENAI_API_BASE`: The base URL of your Azure OpenAI services resource, i.e the Endpoint, e.g. `https://<your_oai_services_name>.openai.azure.com/`.
    - [ ] `OPENAI_API_TYPE`: `azure`. (If for some reason you are using a different provider, you can change this.)
    - [ ] `GPT_35_TURBO_INSTRUCT_MODEL_NAME`: The deployment name of your `gpt-35-turbo-instruct` model.
    - [ ] `GPT_35_CHAT_MODEL_NAME`: The deployment name of your `gpt-35-turbo` model.
    - [ ] `GPT_4_MODEL_NAME`: The deployment name of your `gpt-4o-mini` model.
    - [ ] `WEATHER_API_KEY`: The key for the weather API used in `04_agents`. A key can be attained from https://www.weatherapi.com on the [free plan](https://www.weatherapi.com/pricing.aspx).
    - [ ] `NEWS_API_KEY`: The key for the news API used in `04_agents`. A key can be attained from https://www.newsapi.com on the [free plan](https://newsapi.org/pricing).

### After each training day
- [ ] Reset the Azure OpenAI API key to prevent abuse outside the training ([how to](how-to-reset-openai-api-keys.md)).

### Before each training day
- [ ] Update the GitHub Codespaces secrets with the new Azure OpenAI API key.

### After the training
- [ ] Delete the Azure OpenAI services resource since we have a limited quota for the models.
- [ ] Delete the `academy-llm-applications-<company-name>` resource group on the [gdd_sso](https://github.com/godatadriven/gdd_sso) repo.
- [ ] Remove/regenerate the API keys from NewsAPI & WeatherAPI
- [ ] I validated the API keys no longer work by trying to make an API call using the old API key.


## How-to guides

### Azure OpenAI how-to guides
- [How to deploy Azure OpenAI services infrastructure](how-to-deploy-aoi-infrastructure.md)
- [How to deploy a model to Azure OpenAI services](how-to-deploy-aoi-models.md)
- [How to ensure each model deployment has enough quotas](how-to-ensuring-each-model-deplotment-has-enough-quota.md)
- [How to obtain openai API keys](how-to-obtain-openai-api-keys.md)
- [How to reset the openai API key](how-to-reset-openai-api-keys.md)
