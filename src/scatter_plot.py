import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# Check if file path is provided
if len(sys.argv) != 2:
    print("Usage: python scatter_plot.py <file_path>")
    sys.exit()

# Load the data
file_path = sys.argv[1]
data = pd.read_csv(file_path)

# Select only numeric columns
numeric_data = data.select_dtypes(include=[np.number])

# Calculate the correlation matrix
correlation_matrix = numeric_data.corr()

# Unstack the correlation matrix into a Series, sort it, and remove duplicates
correlations = correlation_matrix.unstack().sort_values(ascending=False).drop_duplicates()

# Remove the perfect correlations (1.0) of a feature with itself
correlations = correlations[correlations < 1.0]

# Get the features with the highest correlation
feature1, feature2 = correlations.idxmax()

# Create the scatter plot
plt.scatter(numeric_data[feature1], numeric_data[feature2])
plt.xlabel(feature1)
plt.ylabel(feature2)

# Display the plot
plt.show()