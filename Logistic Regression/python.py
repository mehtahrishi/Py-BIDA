import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

# Load dataframe
df = pd.read_csv("Sample.csv")

# Create logistic regression model
X = df["var2"]
y = df["var1"]
X = sm.add_constant(X)

# Apply regularization
logistic_model = sm.Logit(y, X).fit_regularized(alpha=0.1)

# Data frame with var2 in ascending order
var2_range = np.linspace(df["var2"].min(), df["var2"].max(), 500)
Predicted_data = pd.DataFrame({"var2": var2_range})

# Fill predicted values using regression model
Predicted_data["var1"] = logistic_model.predict(sm.add_constant(Predicted_data["var2"]))

# Plot Predicted data and original data points
plt.figure(figsize=(10, 6))
plt.scatter(df["var2"], df["var1"], color="blue", label="Original Data")
plt.plot(Predicted_data["var2"], Predicted_data["var1"], color="green", linewidth=2, label="Logistic Regression")
plt.title("Logistic Regression")
plt.xlabel("var2")
plt.ylabel("var1")
plt.legend()
plt.savefig("logistic_regression_python.png")
plt.show()