# How to deploy the Azure Open AI infrastructure
Deploying the Azure Open AI infrastructure is a two-step process:
1. Creating a training-specific resource group in the training subscription.
2. Deploying the Azure Open AI infrastructure.

## Creating a training-specific resource group in the training subscription
1. First clone the [gdd_sso](https://github.com/godatadriven/gdd_sso) repo.
2. Create a new branch, e.g. `academy-llm-applications-<company-name>`.
3. Create a new file: `azure_ad/projects/azureoai-academy-llm-applications-<company-name>.yaml` and fill based on the template below.
4. Commit and push the file to the branch.
5. Create a pull request.
6. Wait for the CI to pass. This can take a while (+-1h). If something file ask Niels for help.
7. When the CI has passed, merge the pull request.
8. Wait for the CD to finish. This can take a while (+-1h). If something file ask Niels for help.

Important:
- The resource group name must be globally unique, so make sure to use a unique name.
- If you want to make other people also owner of the resource group, add them to the `owners` list in the `azure_ad/projects/azureoai-academy-llm-applications-<company-name>.yaml` file.
- If you want to give people read-only access to the resource group, add them to the `users` list in the `azure_ad/projects/azureoai-academy-llm-applications-<company-name>.yaml` file.
- Check the model [availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and [pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/openai-service/#pricing) before deciding upon a region.

The yaml file should look like this:
```yaml
project:
  name: azureoai-academy-llm-applications-<company-name>
  region: "Sweden Central"
  owners:
    - <your-name>@xebia.com
  users:
```

## Deploying the Azure Open AI resource inside the resource group
Now that we have created a training-specific resource group, we can deploy the Azure Open AI resource inside it.
To do this, we will take the following steps:

1. Head to the [Azure portal](https://portal.azure.com/#home) and switch from the `Xebia` subscription to `Xebia Data`. This prevents accidental data leaks to participants. Click [here](./how-to-switch-to-the-training-subscription.md) for instructions on how to switch to the training subscription.
2. In the search bar, search for and click on the `Azure OpenAI` service.
3. Click on the `+ Create` button.
4. Fill in the following on the `Basics` tab:
   - **Subscription**: `Xebia Data`
   - **Resource group**: `azureoai-academy-llm-applications-<company-name>`
   - **Region**: `Sweden Central` (alternative regions can be used but make sure it is the same as the region you specified in the `azure_ad/projects/azureoai-academy-llm-applications-<company-name>.yaml` file; model pricing and availability can be checked [here](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/openai-service/#pricing))
   - **Name**: `azureoai-academy-llm-applications-<company-name>` (must be globally unique, so make sure to use a unique name)
   - **Pricing tier**: `Standard S0`.
   Click next.
5. Fill in the following on the `Network` tab:
   - **Type**: All networks, including the internet, can access this resource.
   Click next.
6. Skip past the section asking for tags.
6. Go to the `Review + create` tab and click on the `Create` button.

After a few minutes, the resource should be deployed and your OpenAI resource should be ready to use.

From now on, it should appear in the list of `Azure OpenAI` resources.
