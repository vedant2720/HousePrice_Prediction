import mlflow
from mlflow.tracking import MlflowClient

mlflow.set_tracking_uri("http://3.110.84.40:5000")
client = MlflowClient()

# Find the latest version of the model
latest_version = client.get_latest_versions("HousePriceModel")[0].version
model_uri = f"models:/HousePriceModel/{latest_version}"

# Download it locally into a folder called 'model_dir'
mlflow.artifacts.download_artifacts(artifact_uri=model_uri, dst_path="model_dir")
print(f"Downloaded model version {latest_version} to model_dir/")