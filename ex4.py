import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Create a synthetic dataset for demonstration
np.random.seed(42)
data_size = 500
features = {
    'Feature_1': np.random.rand(data_size) * 100,
    'Feature_2': np.random.rand(data_size) * 50,
    'Feature_3': np.random.rand(data_size) * 20
}
df = pd.DataFrame(features)
df['Target'] = 50 + 2 * df['Feature_1'] + 3 * df['Feature_2'] - 1.5 * df['Feature_3'] + np.random.randn(data_size) * 10

# Preprocessing
df.fillna(df.mean(), inplace=True)

# Feature Scaling
scaler = StandardScaler()
features_to_scale = df.drop('Target', axis=1).columns
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Split the Dataset
X = df.drop('Target', axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Make Predictions
y_pred = model.predict(X_test)

# Calculate Metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Model Performance Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R2): {r2:.4f}")

# Create Plots
# Actual vs. Predicted Plot
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs. Predicted Values Scatter Plot")
plt.show()

# Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(10, 6))
sns.residplot(x=y_pred, y=residuals, lowess=True, line_kws={'color': 'red', 'lw': 1, 'alpha': 0.8})
plt.title("Residual Plot")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.axhline(y=0, color='gray', linestyle='--')
plt.show()