# Azure Experiments

## Run the Foundry project listing

1. Install the project dependencies:

   ```bash
   python -m pip install -e .
   ```

2. Add your Microsoft Foundry project endpoint to the local `.env` file:

   ```dotenv
   AZURE_AI_PROJECT_ENDPOINT=https://<your-project-endpoint>
   ```

   Use the endpoint shown on your Foundry project's overview page. `.env` is
   local configuration and is ignored by Git.

3. Sign in with the Azure CLI, then run the script:

   ```bash
   az login
   python main.py
   ```

   Run these commands with the project's Python environment activated.