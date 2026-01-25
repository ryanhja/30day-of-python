# Day 13: 30 Days of python programming

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_number = [n for n in numbers if n <= 0]

print(negative_number)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_number = [n for row in list_of_lists for n in row]

print(list_number)

list_tuples = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4) for i in range(11)]

print(list_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_codes = {
    'Finland': 'FIN',
    'Sweden': 'SWE',
    'Norway': 'NOR'
}

countries_upper = [
    [country.upper(), countries_codes[country], city.upper()]
    for row in countries
    for country, city in row
]

print(countries_upper)


countries_dict = [
    {"country": country.upper(), "city": city}
    for row in countries
    for country, city in row
]

print(countries_dict)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list = [
    first_name + " " + last_name
    for rows in names
    for first_name, last_name in rows ]

print(names_list)

slope = lambda a, b: int((- b) / a)
print(slope(2, 2))