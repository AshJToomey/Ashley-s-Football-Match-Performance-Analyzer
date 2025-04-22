import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("match_stats.csv")

# Calculate Pass Accuracy
df["Pass Accuracy (%)"] = (df["Passes Completed"] / df["Passes Attempted"]) * 100

# Display top stats
print("Top Performers:")
print(df[["Player", "Team", "Goals", "Assists", "Pass Accuracy (%)", "Tackles"]])

# Player with highest pass accuracy
best_passer = df.loc[df["Pass Accuracy (%)"].idxmax()]
print(f"\nBest Pass Accuracy: {best_passer['Player']} ({best_passer['Pass Accuracy (%)']:.2f}%)")

# Player with most goals
top_scorer = df.loc[df["Goals"].idxmax()]
print(f"Top Scorer: {top_scorer['Player']} ({top_scorer['Goals']} goals)")

# Visual: Goals by Player
plt.figure(figsize=(8, 5))
plt.bar(df["Player"], df["Goals"], color='green')
plt.title("Goals by Player")
plt.ylabel("Goals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
