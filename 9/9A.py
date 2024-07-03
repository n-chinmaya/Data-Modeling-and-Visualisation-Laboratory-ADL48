import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# i. Visualize the dataset using plot()
print("Dataset:")
print(df)

# ii. Draw the Scatter plot for the dataset on any column
plt.scatter(df['Age'], df['Score'])
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Scatter Plot of Age vs Score')
plt.show()

# iii. Display the scatter plot with different colors
colors = ['red', 'green', 'blue', 'yellow']
plt.scatter(df['Age'], df['Score'], c=colors)
plt.xlabel('Age')
plt.ylabel('Score')
plt.title('Scatter Plot of Age vs Score with different colors')
plt.show()

# iv. Draw the Histogram for the dataset on any column
plt.hist(df['Score'], bins=5)
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title('Histogram of Scores')
plt.show()