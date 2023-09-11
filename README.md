# ML model Deployment using GitHub Action on Azure ML Studio

### In this tutorial, we will deploy ml model as a real-time managed endpoint in Azure ML Studio using GitHub Action.

## Prerequistes
- [Azure Subscription ID & Tenant ID](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id)
- [Azure service principles (Application Client ID & Secret)](https://learn.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli)
- [Azure Machine Learning Workspace](https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources?view=azureml-api-2)

## What is Azure ML Studio?
Azure Machine Learning Studio is a GUI-based integrated development environment for constructing and operationalizing Machine Learning workflow on Azure. It's a cloud service for accelerating and managing the machine learning project lifecycle.
[Please see this azure official documentation for more information.](https://learn.microsoft.com/en-us/azure/machine-learning/overview-what-is-azure-machine-learning?view=azureml-api-2)

## Directory Structure:
#### Folder [environment]
- includes conda environment yaml file to install dependencies to run ml model
#### Folder [model]
- includes trained model
#### Folder [onlinescoring]
- python file that contains the logic about how to run the model and read the input data. [please see this for more information.](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-batch-scoring-script?view=azureml-api-2&tabs=cli#understanding-the-scoring-script)
#### Folder [.github/workflows]
- includes model_deployment.yaml: yaml file for github action automation
#### File [sample-request.json]
- test input data to score by using model
#### File [requirements.txt]
- python dependency to run deployment script from your local or GitHub runner
#### File [model-deployment-azure.py] 
- python file to deploy to azure machine learning studio

**Kindly take a moment to review the comments in the files.**

## GitHub Action Setup
### Configure Azure Information as Secrets in GitHub Action
- Secrets for this tutorial.
  <img title="ML Deployment Secrets" alt="Alt text" src="/secrets-sample.png"> 
- [You can learn more about GitHub Action Secrets in this documentation.](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
### You can change your model endpoint and deployment name in model-deployment-azure.py
- ```python
   ....
   # define an endpoint and deployment name
   endpoint_name = <your endpoint name>
   deployment_name = <your deployment name>
   ....
  ```
### Trigger your GitHub action workflow to deploy model
- Only manual trigger for main branch includes in this repo.
- [You can learn more about Triggering GitHub Action Workflow in this documentation.](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)
