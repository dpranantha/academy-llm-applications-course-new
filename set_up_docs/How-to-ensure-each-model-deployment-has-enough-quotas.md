# How to ensure each model deployment has enough quotas
The Azure OpenAI enforces rate limits on the number of requests you can make per minute.
The entire subscription has a maximum request quota (typically between 120k and 240k tokens per minute).
If there are multiple deployments in the subscription, the quota is shared between them.
So before the training, make sure you have enough pieces of the available quota, e.g., 4K per minute per person.
You can do this as follows:
1. In the search bar, search for and click on the `Azure OpenAI` service.
2. You should now see an overview of all the deployed `Azure OpenAI` resources. Click on the resource you just created.
3. Go to the Azure OpenAI Studio by clicking on the `Go to OpenAI Studio` button.
4. Go to the Quota page by clicking on the `Management > Quota` button in the left menu.
   ![aoi-overview-page-quota.jpg](assets%2Faoi-overview-page-quota.jpg)
5. Here you see an overview of the quota usage over the entire subscription. In this overview, find the models you are interested in and check if you have enough assigned quota.
   ![aoi-overview-page-quota-per-model-type.jpg](assets%2Faoi-overview-page-quota-per-model-type.jpg)
6. If you do not have enough quotas, you will have to redistribute the quota by lowering someone else's quota and increasing your own:
   1. Click on the model type you want to redistribute the quota for. This gives you an overview of all the deployments of this model type.
   2. Click on the deployment you want to take quota from. This opens a form where you can change the quota (it might be hidden behind the `Advanced option` button). Reduce the quota and click on the `Save and close` button.
   3. Click on the deployment you want to give quota to. This opens a form where you can change the quota (it might be hidden behind the `Advanced option` button). Increase the quota and click on the `Save and close` button.
   ![aoi-overview-page-quota-adjustment-form.jpg](assets%2Faoi-overview-page-quota-adjustment-form.jpg)