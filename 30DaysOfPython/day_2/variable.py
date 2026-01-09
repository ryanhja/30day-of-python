# Day 2: 30 Days of python programming

#Level 1 : Declare variable
first_name = "Rayan"
last_name = "HAJANANTENAINA"
full_name = "Rayan HAJANANTENAINA"
country = "Madagascar"
city = "Antananarivo"
age = 24
year = 2026
is_married = False
is_true = True
is_light_on = True
nb_1, nb_2, nb_3 = 41, 72, 36

#Level 2
#1 - Type of variable
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2 - Length variable
print(len(first_name))
print(len(last_name))

#3 - Compare variable length
print(len(first_name) == len(last_name))

#4 - Declare variable
num_one = 5
num_two = 4

#5 - Addition
total = num_one + num_two

#6 - Subtraction
diff = num_two - num_one

#7 - Multiplication
product = num_one * num_two

#8 - Division
division = num_one / num_two

#9 - Modulus
remainder = num_one % num_two

#10 - Power
exp = num_one ** num_two

#11 - Floor
floor_division = num_one // num_two

#12 - i - Are of circle

area_of_circle = 3.14 * (30 ** 2) # Pi * r ^ 2

#12 - ii - Circum of circle
circum_of_circle = round((2 * 3.14 * 30), 5)  # 2Pi * r

#12 - iii - Radius for user
radius = int(input("Enter radius : "))
area_of_circle_2 = 3.14 * (radius ** 2) # Pi * r ^ 2

#13 - Value from user
first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
country = input("Enter country : ")

#14 - Help keywords
help('keywords')