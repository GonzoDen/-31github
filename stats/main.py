import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'df' with columns 'Skill', 'Gender', and 'Percentage'
# 'Percentage' represents the percentage of respondents for each combination of skill and gender

# Sample DataFrame (replace this with your actual data)
data = {
    'Skill': ['Skill1', 'Skill1', 'Skill2', 'Skill2', 'Skill3', 'Skill3'],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Percentage': [20, 30, 40, 50, 60, 70]
}

df = pd.DataFrame(data)

# Pivot the DataFrame to get it in the right format for the heatmap
heatmap_data = df.pivot(index='Skill', columns='Gender', values='Percentage')

# Create a heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm', fmt=".1f", linewidths=.5)

# Customize labels and title
plt.xlabel('Gender')
plt.ylabel('Skill')
plt.title('Heatmap for Skill and Gender Associations')

# Show the plot
plt.show()
