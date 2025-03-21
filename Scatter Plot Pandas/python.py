import pandas as pd
import matplotlib.pyplot as plt
import os  # Import the os module for file path operations

# reading the database
data = pd.read_csv("tips.csv")

# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'])

# Adding Title to the Plot
plt.title("Scatter Plot")

# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

# Add colorbar
plt.colorbar()

plt.savefig("scatter_plot_day_tip.png")

# Show the plot (optional)
plt.show()