from automated_data_analysis import analyze_data

df = analyze_data(
    'sample.csv',
    fill_strategy={"Age": "median", "Salary": "mean"},
    stats_columns=["Age", "Salary"],
    stats=["mean", "median", "min", "max"]
)
