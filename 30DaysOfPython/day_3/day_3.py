# Day 3: 30 Days of python programming

print("Exercise 01:")
age = 26
print("Age = ",age)

print("\nExercise 02:")
height = 72.5
print("Height = ",height)

print("\nExercise 03:")
number_1 = 1 + 1j
print("complex number = ", number_1)

print("\nExercise 04:")
b = int(input("Enter base : "))
h = int(input("Enter height : "))

area = 0.5 * b * h

print("The area of the triangle is ", area)

print("\nExercise 05:")
side_a = int(input("Enter side a : "))
side_b = int(input("Enter side b : "))
side_c = int(input("Enter side c : "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is ", perimeter)

print("\nExercise 06:")
r_length = int(input("Enter length : "))
r_width = int(input("Enter width : "))

r_area = r_length * r_width
r_perimeter = 2 * (r_length + r_width)

print("The area of the rectangle is", r_area)
print("The perimeter of the rectangle is", r_perimeter)

print("\nExercise 07:")
c_radius = int(input("Enter radius : "))
pi = 3.14
c_area = pi * c_radius * c_radius
c_circumference = 2 * pi * c_radius

print("The area of circle is ", c_area)
print("The circumference of circle is ", c_circumference)

print("\nExercise 08:")
# y = 2x - 2
a = 2
b = -2

#If x = 0 => y = a (0) + b
x0 = 0
y = a * x0  + b

#If y = 0 => x = - b / a
x = (- b) / a
x = int(x)

print(f"x-intercept = ({x}, 0)")
print(f"y-intercept = (0, {y})")

print("\nExercise 09:")
# m = y2 - y1 / x2 - x1
x1, x2 = 2, 6
y1, y2 = 2, 10

m = (y2 - y1) / (x2 - x1)
m = int(m)
print("slope (m) = ",m)

#Length comparison
print("\nExercise 10:")
str_a = "python"
str_b = "dragon"
print("Is length :",len(str_a) == len(str_b))

#Matrice table
print("\nExercise 11:")
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)