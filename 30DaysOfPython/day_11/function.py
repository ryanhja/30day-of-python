# Day 11: 30 Days of python programming
from ipaddress import summarize_address_range

print("sum of two numbers")
def add_two_numbers(nb_1, nb_2):
    return nb_1 + nb_2


print(add_two_numbers(21, 23))

print("\nArea of circle")
def area_of_circle(r):
    return 3.14 * r * r


print(area_of_circle(2))

print("sum all numbers")
def add_all_nums(*args):
    sum_number = 0
    for i in args:
        sum_number += i

    return sum_number


print(add_all_nums(1, 2, 3, 5))

print("\nCelsius to fahrenheit")
def convert_celsius_to_fahrenheit(temperature):
    fahrenheit = (temperature * 9 / 5) + 32
    return fahrenheit


print(convert_celsius_to_fahrenheit(5))

print("Check season")
def check_season(month: str):
    month = month.title()

    seasons = {
        'Winter': ['December', 'January', 'February'],
        'Spring': ['March', 'April', 'May'],
        'Summer': ['June', 'July', 'August'],
        'Autumn': ['September', 'October', 'November']
    }

    for season, months in seasons.items():
        if month in months:
            return season
    return None


print(check_season(month="April"))