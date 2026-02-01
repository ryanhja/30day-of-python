# Day 17: 30 Days of python programming


try:
    age = input("Date of birth : ")
    print("Hello", first_name, "You are", (2026 - age))
except NameError as e:
    print("NameError : ", e)
except TypeError as e:
    print("TypeError : ", e)
except Exception as e:
    print(e)


print("Enumerate")
try:
    countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
    for index, item in enumerate(countries):
        print(index, item)
except Exception as e:
    print(e)

print(" \nZip")
try:
    fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
    vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
    fruits_and_veges = []
    for f, v in zip(fruits, vegetables):
        fruits_and_veges.append({'fruit': f, 'veg': v})

    print(fruits_and_veges)
except Exception as e:
    print(e)
