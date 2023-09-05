# import required libraries
import os
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    Model,
    Environment,
    CodeConfiguration,
)
from azure.identity import DefaultAzureCredential

# details of Azure Machine Learning workspace
subscription_id = os.environ['AZ_SUBSCRIPTION_ID']
resource_group = os.environ['AZ_RESOURCE_GP_NAME']
workspace_name = os.environ['AZ_ML_WORKSPACE_NAME']

# get a handle to the workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace_name
)

# define an endpoint and deployment name
endpoint_name = "demo-endpoint"
deployment_name = "demodeployment"

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name = endpoint_name,
    description="this is a demo endpoint",
    auth_mode="key"
)

## deployment configuration
model = Model(path="model-requirements/model/sklearn_regression_model.pkl")
env = Environment(
    conda_file="model-requirements/environment/conda.yaml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest",
)

model_deployment = ManagedOnlineDeployment(
    name=deployment_name,
    endpoint_name=endpoint_name,
    model=model,
    environment=env,
    code_configuration=CodeConfiguration(
        code="model-requirements/onlinescoring", scoring_script="score.py"
    ),
    instance_type="Standard_DS1_v2",
    instance_count=1,
)

## deploy to azure
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
ml_client.online_deployments.begin_create_or_update(model_deployment).result()

# # demo model deployment takes 100 traffic
endpoint.traffic = {deployment_name: 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# check the status of the endpoint
azure_deployment_verify = ml_client.online_endpoints.get(name=endpoint_name)
print(f"\nAzure Deployment Info: \n{azure_deployment_verify}\n")

# test the blue deployment with some sample data
azure_deployment_scoring = ml_client.online_endpoints.invoke(
    endpoint_name=endpoint_name,
    deployment_name=deployment_name,
    request_file="model-requirements/sample-request.json",
)
print(f"Scoring Result: \n{azure_deployment_scoring}\n")

# # check the status of the online deployment
azure_deployment_logs =ml_client.online_deployments.get_logs(
    name=deployment_name, endpoint_name=endpoint_name, lines=50
)
print(f"Azure Deployment Logs: \n{azure_deployment_logs}")
