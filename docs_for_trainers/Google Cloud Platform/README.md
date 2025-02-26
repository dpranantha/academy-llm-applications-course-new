# Google Cloud Platform

## GCP Project setup

To setup the codespaces, follow these steps:

1. Fork the repository into a new repo and give it a clear name, such as `academy-llm-applications-bol`.
2. Visit `https://console.cloud.google.com/projectcreate` and create a new Google project for the training (in the location `xebia.com > xebia-data-nl > Playground`).
3. Go to `https://console.cloud.google.com/apis/`. gcloud Enable the `Vertex AI API` and `Generative Language API` in your GCP project.
4. Go to `https://console.cloud.google.com/apis/credentials` and click on `CREATE CREDENTIALS` > `API KEY` to generate a new key.
5. Copy the API key and temporarily store it in a secure location.
6. Edit the API key (click ⋮ under actions) to restrict access to only the `Vertex AI API` and `Gemini API`/`Generative Language API`.
7. Go to `https://github.com/godatadriven/<YOUR REPO NAME>/settings/secrets/codespaces` and click on `New repository secret`.
8. Save the API Key with the name `GOOGLE_API_KEY` and the value you copied from Google Cloud.

To test your setup, open GitHub Codespaces and run `exercises/01_basic_concepts/extras/00_gcloud_connection_test.ipynb`. Remember to delete the API key and the Google project after completing the training.

Note:
- Codespace container needs to be rebuilt after setting the API key secret.