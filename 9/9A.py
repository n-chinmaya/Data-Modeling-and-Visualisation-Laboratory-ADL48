import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'], 
        'Age': [28, 24, 35, 32], 
        'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# Visualize the dataset using plot()
plt.plot(df['Age'])
plt.title('Age Distribution')
plt.xlabel('Index')
plt.ylabel('Age')
plt.show()

# Draw the Scatter plot for the dataset on any column
plt.scatter(df['Age'], df['Score'])
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()

# Display the scatter plot with different colors
colors = ['red', 'green', 'blue', 'yellow']
plt.scatter(df['Age'], df['Score'], c=colors)
plt.title('Age vs Score with Different Colors')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()

# Draw the Histogram for the dataset on any column
plt.hist(df['Score'], bins=5)
plt.title('Score Distribution')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()