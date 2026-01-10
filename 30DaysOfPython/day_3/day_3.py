# Day 3: 30 Days of python programming

age = 26
height = 72.5
number_1 = 1j

b = int(input("Enter base : "))
h = int(input("Enter height : "))

area = 0.5 * b * h

print("The area of the triangle is ", area)

side_a = int(input("Enter side a : "))
side_b = int(input("Enter side b : "))
side_c = int(input("Enter side c : "))

perimeter = side_a + side_b + side_c

print("The perimeter of the triangle is ", perimeter)

r_length = int(input("Enter length : "))
r_width = int(input("Enter width : "))

r_area = r_length * r_width
r_perimeter = 2 * (r_length + r_width)

print("The area of the rectangle is", r_area)
print("The perimeter of the rectangle is", r_perimeter)

c_radius = int(input("Enter radius : "))
pi = 3.14
c_area = pi * c_radius * c_radius

print("The area of circle is ", c_area)

c_circumference = 2 * pi * c_radius
print("The circumference of circle is ", c_circumference)