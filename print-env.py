import os

# details of Azure Machine Learning workspace
subscription_id = os.environ['AZ_SUBSCRIPTION_ID']
resource_group = os.environ['AZ_RESOURCE_GP_NAME']
workspace_name = os.environ['AZ_ML_WORKSPACE_NAME']

print(subscription_id)
print(resource_group)
print(workspace_name)