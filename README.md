# ⚽ Match Stats Analyzer

A simple Python script for analyzing football player performance data using `pandas` and `matplotlib`.

## 📊 Features

- Calculates pass accuracy for each player
- Identifies:
  - The player with the **highest pass accuracy**
  - The **top goal scorer**
- Displays top performance metrics (Goals, Assists, Pass Accuracy, Tackles)
- Visualizes goals scored by each player in a bar chart

## 🗂️ Input Data

Make sure your `match_stats.csv` file includes the following columns:

- `Player`
- `Team`
- `Goals`
- `Assists`
- `Passes Completed`
- `Passes Attempted`
- `Tackles`

Example:
```csv
Player,Team,Goals,Assists,Passes Completed,Passes Attempted,Tackles
John Smith,Team A,3,1,50,60,4
...
