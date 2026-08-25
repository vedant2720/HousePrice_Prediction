import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Dummy data
X, y = np.array([[1], [2], [3]]), np.array([1.2, 1.9, 3.2])

mlflow.set_tracking_uri("http://3.110.84.40:5000")
mlflow.set_experiment("House_Price_Project")

with mlflow.start_run():
    model = LinearRegression()
    model.fit(X, y)

    predictions = model.predict(X)
    mse = mean_squared_error(y, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, predictions)

    mlflow.log_param("training_samples", len(X))
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2_score", r2)

    # Log AND Register the model in MLflow
    mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="model",
        registered_model_name="HousePriceModel"
    )
    print("Model trained and registered to EC2 MLflow!")
    print(f"Metrics: mse={mse:.4f}, rmse={rmse:.4f}, r2_score={r2:.4f}")