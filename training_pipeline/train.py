import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy data
X, y = np.array([[1], [2], [3]]), np.array([1.2, 1.9, 3.2])

mlflow.set_tracking_uri("http://3.110.84.40:5000")
mlflow.set_experiment("House_Price_Project")

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X, y)
    
    # Log AND Register the model in MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="HousePriceModel" # <-- This registers it in MLflow
    )
    print("Model trained and registered to EC2 MLflow!")