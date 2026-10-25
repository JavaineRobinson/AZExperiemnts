import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

with AIProjectClient(
    endpoint = os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential = DefaultAzureCredential()
) as client:
    print("Successfully connected to Micrisoft Foundry Proejct")

    deployments = list(client.deployments.list())
    for deployment in deployments:
        print(f"Deployment name: {deployment.name}, status: {deployment.status}")