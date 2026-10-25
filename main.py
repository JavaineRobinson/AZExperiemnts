import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
if not endpoint:
    raise ValueError(
        "AZURE_AI_PROJECT_ENDPOINT is not set. Add your Microsoft Foundry "
        "project endpoint to the .env file."
    )

with AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
) as client:
    print("Successfully connected to Microsoft Foundry Project")

    deployments = list(client.deployments.list())
    for deployment in deployments:
        print(f"Deployment name: {deployment.name}")