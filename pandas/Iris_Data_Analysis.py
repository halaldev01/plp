
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the iris dataset
iris_data = load_iris()
iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
iris['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

# Set seaborn theme
sns.set(style="whitegrid")

# Create a figure with 2x2 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Iris Dataset Visualizations", fontsize=16)

# Line Chart: Average sepal length per sample index for each species
for species in iris['species'].unique():
    subset = iris[iris['species'] == species]
    axs[0, 0].plot(subset.index, subset['sepal length (cm)'], label=species)
axs[0, 0].set_title("Line Chart: Sepal Length by Index")
axs[0, 0].set_xlabel("Sample Index")
axs[0, 0].set_ylabel("Sepal Length (cm)")
axs[0, 0].legend()

# Bar Chart: Average petal length per species
sns.barplot(data=iris, x="species", y="petal length (cm)", ax=axs[0, 1], palette="viridis")
axs[0, 1].set_title("Bar Chart: Avg Petal Length by Species")
axs[0, 1].set_ylabel("Avg Petal Length (cm)")
axs[0, 1].set_xlabel("Species")

# Histogram: Distribution of sepal width
sns.histplot(iris['sepal width (cm)'], bins=15, kde=True, ax=axs[1, 0], color='orange')
axs[1, 0].set_title("Histogram: Sepal Width Distribution")
axs[1, 0].set_xlabel("Sepal Width (cm)")
axs[1, 0].set_ylabel("Frequency")

# Scatter Plot: Sepal length vs Petal length
sns.scatterplot(data=iris, x="sepal length (cm)", y="petal length (cm)", hue="species", ax=axs[1, 1], palette="deep")
axs[1, 1].set_title("Scatter Plot: Sepal Length vs Petal Length")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
