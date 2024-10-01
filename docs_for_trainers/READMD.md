# Docs for trainers
This folder contains documentation for trainers.
Here you find information on how to set up the training infrastructure, how to prepare for the training and several how-to guides.


## Checklist for the training
Bellow you find a checklist that helps you to prepare for the training.
Make you don't forget anything by checking off the items on the list.
It also contains links to the relevant how-to guides if you need more information.

### Before the training
- [ ] I have created a new repo specifically for this training using this repo as a template ([how to](how-to-setup-new-repo-and-code-spaces.md)).
- [ ] I have created a new Azure OpenAI services resource for this training ([how to](how-to-deploy-aoi-infrastructure.md)).
- [ ] I have deployed the following models to the Azure OpenAI services resource ([how to](how-to-deploy-aoi-models.md)):
    - [ ] The chat model: `gpt-35-turbo`.
    - [ ] The text completion model: `gpt-35-turbo-instruct`.
    - [ ] The text completion base model: `babbage-002`.
- [ ] I have validated the models have a reasonable quota ([how to](How-to-ensure-each-model-deployment-has-enough-quotas.md)).
- [ ] I obtained the following environment variables and added them as GitHub CodeSpaces secrets ([how to](how-to-set-github-codespace-secrets.md)):
    - [ ] `OPENAI_API_KEY`: The API key of your Azure OpenAI services resource (see [how to](how-to-obtain-openai-api-keys.md)).
    - [ ] `OPENAI_API_BASE`: The base URL of your Azure OpenAI services resource, i.e the Endpoint, e.g. `https://<your_oai_services_name>.openai.azure.com/`.
    - [ ] `OPENAI_API_TYPE`: `azure`. (If for some reason you are using a different provider, you can change this.)
    - [ ] `GPT_35_TURBO_INSTRUCT_MODEL_NAME`: The deployment name of your `gpt-35-turbo-instruct` model.
    - [ ] `GPT_35_CHAT_MODEL_NAME`: The deployment name of your `gpt-35-turbo` model.
    <!-- - [ ] `GPT_35_CHAT_MODEL_16K_NAME`: The deployment name of your `gpt-35-turbo-16k` model. -->
    - [ ] `BABBAGE_MODEL_NAME`: The deployment name of your `babbage-002` model.
    - [ ] `WEATHER_API_KEY`: The key for the weather API used in `04_agents`. A key can be attained from https://www.weatherapi.com on the [free plan](https://www.weatherapi.com/pricing.aspx).
    - [ ] `NEWS_API_KEY`: The key for the news API used in `04_agents`. A key can be attained from https://www.newsapi.com on the [free plan](https://newsapi.org/pricing).
- [ ] I have validated all the solutions notebooks run without errors using the GitHub CodeSpaces environment variables to ensure that the infrastructure is set up correctly.
- [ ] I have duplicated my own version of the Miro board to use in the training.
    - To do this, first request to join the `GoDataDriven Academy` team, by clicking the plus sign on the left-hand side of the [Miro homepage](https://miro.com/app/dashboard/).
    - Once you are a member, head to the [Miro board template](https://miro.com/app/board/uXjVNABD2U8=/), click on the name of the board in the top-left corner and create a duplicate with a different name.
    - Check that anyone with a link to the board by clicking `share` in the top-right corner of the new board.
- [ ] I have obtained the GitHub handle of the participants. If you don't already have them, ask for them in your introductory email.
- [ ] I have sent out a Teams/Zoom link to the participants if they are attending online.
- [ ] 1 or 2 days before the start of the training, I have added the participants to the repo as collaborators with write access.
    - To do this, go to the `godatadriven/academy-llm-applications-<training_name>` repoo and click the `settings` icon in the top-right corner.
    - Navigate to `Access` > `Collaborators and Teams`.
    - Under `Manage Access`, click `Add people`, enter the GitHub handle and select `write` access.

### After each training day
- [ ] Reset the Azure OpenAI API key to prevent abuse outside the training ([how to](how-to-reset-openai-api-keys.md)).

### Before each training day
- [ ] Update the GitHub CodeSpaces secrets with the new Azure OpenAI API key.

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

### GitHub and CodeSpaces how-to guides
- [How to set GitHub CodeSpace secrets](how-to-set-github-codespace-secrets.md)
- [How to set up new repo and Code Spaces](how-to-setup-new-repo-and-code-spaces.md)
