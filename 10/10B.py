import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
data = pd.read_csv("iris.csv")  # Assuming the dataset is named "iris.csv" in the same directory

# Display the first 5 rows
print("First 5 rows:\n", data.head())

# Display the last 5 rows
print("\nLast 5 rows:\n", data.tail())

# Display dataset information
print("\nDataset information:\n", data.info())

# Display value overview of each column (descriptive statistics)
print("\nValue overview of each column:\n", data.describe())

data.plot()
plt.show()

print("\nVisualizations generated successfully!")