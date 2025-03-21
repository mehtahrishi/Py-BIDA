import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

x = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
y = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

# Create a pandas DataFrame (optional, but good practice)
data = pd.DataFrame({'x': x, 'y': y})

# Perform linear regression
model = sm.OLS(y, sm.add_constant(x)).fit()  # Add a constant (intercept)

# Print the regression summary (optional)
# print(model.summary())

# Plot the data and regression line
plt.figure()
plt.scatter(x, y, color='blue')
plt.title("Height & Weight Regression")
plt.xlabel("Height in cm")
plt.ylabel("Weight in Kg")

# Get the regression line
predicted_y = model.predict(sm.add_constant(x))

# Plot the regression line
plt.plot(x, predicted_y, color='red')  # Changed color to red for clarity.

plt.savefig("linearregression.png")
plt.show()