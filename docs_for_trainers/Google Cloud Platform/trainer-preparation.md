# Traininer preparation instructions 🧑‍🏫

Are you a participant of the training? Then you can skip this part and hop over to the next notebook.

In order to get all infra in place for the training, you need to provision the following in GCP.
Make sure you create a new GCP project for the training at hand, in which you can provision these resources.
Infra can be provisioned manually. Remove the GCP project afterwards.

- [ ] Enable Vertex AI [API](https://console.cloud.google.com/apis/).

  ![alt text](<../assets/vertexai.png>)

- [ ] Add participants with roles in [IAM](https://console.cloud.google.com/iam-admin/):
  - Editor

  ![add editor in IAM](<../assets/editor.png>)

- [ ] Increase LLM requests/minute [quotas](https://console.cloud.google.com/iam-admin/quotas) if necessary during training
  - Name: "Generate content requests per minute per project per base model per minute per region per base_model"

  ![alt text](<../assets/quota.png>)

  Pick the region you are currently making API calls for.

  e.g. UI example where a region is selected:

  ![alt text](<../assets/ui.png>)

  ... or in your training code:

  ```
  GCP_LOCATION="europe-west4"
  ```

## Optional

Only necessary if you know why you need it.

- [ ] Enable Cloud Trace API

  Required only if you start using doing tracing (in LLMOps this happens).
- [ ] Create service account with roles:
  - Vertex AI User

  Only required if you deploy services in GCP (Cloud Run, etc).

  ![service account creation](<../assets/service-account.png>)

  1. Create a service account
  2. Grant it the role "Vertex AI User"