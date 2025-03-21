import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df.plot(kind='scatter', x='Duration', y='Calories')

plt.savefig("datavisual.png")  # Save the figure first
plt.show()  # Then display it