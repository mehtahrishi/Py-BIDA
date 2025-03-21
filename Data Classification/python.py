import pandas as pd
import matplotlib.pyplot as plt

rainfall = [799, 1174.8, 865.1, 1334.6, 635.4, 918.5, 685.5, 998.6, 784.2, 985, 882.8, 1071]

# Create a pandas DatetimeIndex with monthly frequency starting from January 2021
date_index = pd.date_range(start='2021-01-01', periods=len(rainfall), freq='MS')

# Create a pandas Series from the rainfall data with the DatetimeIndex
rainfall_series = pd.Series(rainfall, index=date_index)

# Print the time series data
print(rainfall_series)

# Plot the time series
plt.figure()
plt.plot(rainfall_series)
plt.title("Rainfall Time Series")
plt.xlabel("Date")
plt.ylabel("Rainfall")
plt.savefig("rainfall.png")  # Save the plot as a PNG file
plt.show() #this line is optional, it will display the graph in console.