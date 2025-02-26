# How to obtain Azure OpenAI API keys

1. Go to the [Azure portal](https://portal.azure.com/).
2. Find your Azure OpenAI services resource.
   1. Click on the search bar and search for `OpenAI`.
   2. Click on the `Azure OpenAI` service.
   3. Click on the resource you created previously.
3. On the resource page, click on the `Keys and Endpoint` tab under `Resource Management`.
![](assets/aoi-resource-page.jpg)
4. Copy the `Key 1` value and store it in (one of) the following places:
   1. If you are doing local development, store it in your `.env` file as the `OPENAI_API_KEY` variable.
   2. If you are working in a GitHub CodeSpace, store it in the GitHub CodeSpace secrets as the `OPENAI_API_KEY` variable. See [How to set GitHub CodeSpace secrets](./how-to-set-github-codespace-secrets.md) for more information.
5. Copy the `Endpoint` value and store it in (one of) the following places:
   1. If you are doing local development, store it in your `.env` file as the `OPENAI_API_BASE` variable.
   2. If you are working in a GitHub CodeSpace, store it in the GitHub CodeSpace secrets as the `OPENAI_API_BASE` variable. See [How to set GitHub CodeSpace secrets](./how-to-set-github-codespace-secrets.md) for more information.

   ![](assets/aoi-key-and-endpoint-page.jpg)

Note: Azure provides you with two API keys. Both keys are valid and can be used to make API calls.
So it is a good idea to consistently expose only one of the keys to the participants.
This way, you can keep the other key for yourself, and you don't have to worry about resetting your personal key.

