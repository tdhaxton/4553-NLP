import pandas as pd

df = pd.read_csv("ds_salaries.csv", sep = ",")

print(df.head())

#find the largest value in "remote_ratio"
print(df["remote_ratio"].max())

#find the 5 highest salaries
sorted = df["salary_in_usd"].sort_values()
print(sorted.head())

#How many data points (rows) are in the file?
print(df.info())

print(df.describe())

#How many employees are fully remote (remote_ratio == 100)
remote = df.query("remote_ratio == 100")
print(len(remote))