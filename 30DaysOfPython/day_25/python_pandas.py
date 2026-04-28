# Day 25: 30 Days of python programming

import pandas as pd
import random

# Series
print("\nSeries")
numbers = [random.randint(1, 100) for _ in range(10)]
indexes = [i for i in range(1, 11)]
df = pd.Series(numbers, index=indexes)

print(df)

# Dict
print("\nDF From Dict")
dct = {"name": "Rayan", "last name": "Steve"}
df = pd.Series(dct)

print(df)

# Constant
print("\nConstant")

df = pd.Series(10, index=indexes)
print(df)

# List
print("\nDF From List")
data = [
    ['Rayan', 'Madagascar', 'Fianarantsoa'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, index=[1, 2, 3], columns=['Names', 'Country', 'City'])
print(df)

# CSV
print("\nDF From List")
df = pd.read_csv('weight-height.csv')
print(df)

# Exploration
print("\nHead")
print(df.head())

print("\nTail")
print(df.tail())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nHeight")
height = df["Height"]

print(height)

print("\nDescribe")
print(df.describe)

# Modifying
print("\nModifying a DataFrame")
data = [
    {"Name": "Rayan", "Country": "Madagascar", "City": "Fianarantsoa"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"}]
data_f = pd.DataFrame(data)
print(data_f)

weight = [45, 78, 62]

data_f["Weight"] = weight

print("\n", data_f)

heights = [173, 175, 169]
data_f['Height'] = heights

print("\nModifying values")
data_f["Weight"] = data_f["Weight"] * 5
print(data_f)


def calculate_bmi():
    weights = data_f['Weight']
    heights = data_f['Height']
    dmi_data = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        dmi_data.append(b)
    return dmi_data


data_f['BMI'] = calculate_bmi()
print("\n", data_f)

print("\nExercise 1")
df_hacker_news = pd.read_csv("hacker_news.csv")
print(df_hacker_news)

print("\nExercise 2")
print(df_hacker_news.head())

print("\nExercise 3")
print(df_hacker_news.tail())

print("\nExercise 4")
print(df_hacker_news["title"])
