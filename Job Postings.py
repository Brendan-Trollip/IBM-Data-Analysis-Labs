import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel(r"C:\Users\Brendan\OneDrive\Documents\IBM Data Analyst\job-postings.xlsx")

# Sort by number of jobs in descending order
df_sorted = df.sort_values(by="Number of Jobs", ascending=False)

# Plot horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(df_sorted["Location"], df_sorted["Number of Jobs"], color="steelblue")
plt.title("Job Postings by Location (Descending Order)")
plt.xlabel("Number of Job Postings")
plt.ylabel("Location")
plt.gca().invert_yaxis()  # largest bar at the top
plt.tight_layout()
plt.show()


