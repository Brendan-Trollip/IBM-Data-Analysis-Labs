import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv(r"C:\Users\Brendan\OneDrive\Documents\IBM Data Analyst\popular-language.csv")

# Inspect the columns to confirm structure
print("Columns in the file:", df.columns)

# Sort by salary in descending order
df_sorted = df.sort_values(by="Average Annual Salary", ascending=False)

# Plot horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(df_sorted["Language"], df_sorted["Average Annual Salary"], color="darkorange")
plt.title("Popular Programming Languages by Salary (Descending Order)")
plt.xlabel("Average Annual Salary")
plt.ylabel("Language")
plt.gca().invert_yaxis()  # highest salary at the top
plt.tight_layout()
plt.show()
