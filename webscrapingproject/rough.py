import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample DataFrame
data = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 3, 5, 7, 11]
}
df = pd.DataFrame(data)

# Create the scatter plot
sns.scatterplot(x='x', y='y', data=df)

# Show the plot
plt.show()
