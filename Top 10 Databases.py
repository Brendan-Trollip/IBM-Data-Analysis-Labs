import pandas as pd
import matplotlib.pyplot as plt

# Load your survey data
df = pd.read_csv(r"C:\Users\Brendan\Downloads\survey-data.csv")

# Split multiple databases into separate rows
db_series = df['DatabaseWantToWorkWith'].dropna().str.split(';').explode().str.strip()

# Count frequency of each database
db_counts = db_series.value_counts().head(10)

# Plot horizontal bar chart
plt.figure(figsize=(8,6))
plt.barh(db_counts.index, db_counts.values, color='lightgreen')
plt.title("Top 10 Databases (Want to Work With)")
plt.xlabel("Number of Respondents")
plt.ylabel("Database")
plt.gca().invert_yaxis()  # largest at the top
plt.tight_layout()
plt.show()
