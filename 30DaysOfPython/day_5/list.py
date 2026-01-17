# Day 5: 30 Days of python programming
from numpy.ma.extras import average

lst = []
print("Empty list : ", lst)

fruits = ['banana', 'orange', 'mango', 'lemon', "apple"]
print("List with 5 items : ", fruits)

print("Length list : ", len(fruits))

print(f"First item = {fruits[0]}, Middle item = {fruits[int(len(fruits) / 2)]}, Last item = {fruits[-1]}")

mixed_data_types = ["Rayan", 26, 72, "Single", {"Country": "Madagascar", "City": "Antananarivo"}]
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

it_companies.append('Samsung')
print(it_companies)

it_companies.insert(int(len(it_companies) / 2), "LinkedIn")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

it_companies_joins = "#; ".join(it_companies)
print(it_companies_joins)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

it_companies.remove(it_companies[0])
print(it_companies)

first_3_itc = it_companies[:3]
print(first_3_itc)

last_3_itc = it_companies[-3:]
print(last_3_itc)

it_companies.remove(it_companies[0])
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(min(ages))
print(max(ages))
print(average(ages))

average_ages = sum(ages)/len(ages)
print(average_ages)
