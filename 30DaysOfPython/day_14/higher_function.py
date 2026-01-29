# Day 14: 30 Days of python programming
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [i for i in range(11)]


def upper_message(msg):
    return msg.upper()


def is_even(nb):
    if nb % 2 == 0:
        return True

    return False


def add_number(x, y):
    return x + y


def multipy_number(x, y):
    return x * y


print("Map")
country_upper = map(upper_message, countries)
print(list(country_upper))

print("\nFilter")
number_even = filter(is_even, numbers)
print(list(number_even))

print("\nReduce")
sum_number = reduce(add_number, numbers)
print(sum_number)

print("\nHigher order function")


def apply_operation(function, x, y):
    func = function(x, y)
    return func


print(apply_operation(add_number, 4, 6))
print(apply_operation(multipy_number, 4, 6))

print("\nClosure")


def multiply_operation(factor):
    def multiply(x):
        return x * factor

    return multiply


double = multiply_operation(2)
print(double(9))

print("\nDecorator")


def uppercase_message(function):
    def wrapper():
        func = function()
        result = func.upper()
        return result

    return wrapper


@uppercase_message
def say_hello():
    return "Hello, world!"


print(say_hello())

print("\nFor loop")

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

print("\nMap countries uppercase")

upper_country = map(lambda x: x.upper(), countries)
print(list(upper_country))

print("\nMap square numbers")

square_number = map(lambda x: x * 2, numbers)
print(list(square_number))

print("\nMap names uppercase")

upper_name = map(lambda x: x.upper(), names)
print(list(upper_name))

print("\nFilter land country")


def is_land(country_name):
    return "land" in country_name


land_country = filter(is_land, countries)
print(list(land_country))

print("\nFilter country six characters")


def is_six(country_name):
    return len(country_name) == 6


country_six_character = filter(is_six, countries)
print(list(country_six_character))

print("\nFilter country start with E")


def is_start_e(country_name):
    return country_name.startswith("E")


country_start_e = filter(is_start_e, countries)
print(list(country_start_e))

print("\nChain list iterators")
sum_numbers_filtered = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x > 5,
        map(
            lambda x: x * 2,
            numbers
        )
    )
)

print(sum_numbers_filtered)

print("\nList string items")


def get_string_lists(list_items):
    result = filter(
        lambda x: x.isalpha(),
        list_items
    )

    return list(result)


items = ["Rayan", "25", "Python", "178.0"]

print(get_string_lists(items))


print("\nJoin countries")
europe_countries = reduce(
    lambda x, y: x + ", " + y,
    countries
)

print(europe_countries + " are north European countries")