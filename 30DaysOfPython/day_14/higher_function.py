# Day 14: 30 Days of python programming
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def upper_message(msg):
    return msg.upper()


def is_even(nb):
    if nb % 2 == 0:
        return True

    return False


def add_number(x, y):
    return x + y


print("Map")
country_upper = map(upper_message, countries)
print(list(country_upper))

print("\nFilter")
number_even = filter(is_even, numbers)
print(list(number_even))

print("\nReduce")
summe_number = reduce(add_number, numbers)
print(summe_number)
