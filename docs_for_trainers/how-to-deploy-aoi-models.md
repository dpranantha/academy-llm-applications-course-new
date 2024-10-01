# How to deploy Azure OpenAI models
The Azure OpenAI resource does not expose any models by default.
You have to select which models you want to use and deploy them.
To do this, take the following steps:
1. In the search bar, search for and click on the `Azure OpenAI` service.
2. You should now see an overview of all the deployed `Azure OpenAI` resources. Click on the resource you just created.
3. Go to the Azure OpenAI Studio by clicking on the `Go to OpenAI Studio` button.
4. Go to the Deployments page by clicking on the `Management > Deployments` button in the left menu.
   ![aoi-overview-page-deployment.jpg](assets%2Faoi-overview-page-deployment.jpg)
6. Click on the `+ Create new deployment` button.
7. Deploy the following models (it is best to keep the deployment and model names the same):
   - GPT base: `babbage-002`.
   - GPT 3.5 chat: `gpt-35-turbo` (Make sure the model version is 0631 or higher).
   <!-- - GPT 3.5 chat 16k: `gpt-35-turbo-16k` (Make sure the model version is 0631 or higher). -->
   - GPT 3.5 text completion: `gpt-35-turbo-instruct`.
   ![aoi-overview-page-deployment-form.jpg](assets%2Faoi-overview-page-deployment-form.jpg)