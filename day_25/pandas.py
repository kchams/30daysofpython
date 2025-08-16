#Exercises: Day 25
#1. Read the hacker_news.csv file from data directory
import pandas as pd

df = pd.read_csv('hacker_news.csv')
print(df)

#2. Get the first five rows
first_five_rows = df.head()
print(first_five_rows)

#3. Get the last five rows
last_five_rows = (df.tail())
print(last_five_rows)

#4. Get the title column as pandas series
title = df.columns
print(title)

#5. Count the number of rows and columns
rows_columns_number = df.shape()
print(rows_columns_number)