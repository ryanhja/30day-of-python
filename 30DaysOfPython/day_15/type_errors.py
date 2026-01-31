# Day 15: 30 Days of python programming

import math

# SyntaxError
try:
    exec('print "Hello"')
except SyntaxError as e:
    print(f"{type(e).__name__} : {e}")

# NameError
try:
    print(firt_name)
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# IndexError
try:
    numbers = [4, 2, 6, 3, 5]
    print(numbers[5])
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# ModuleNotFoundError
try:
    import maths
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# AttributeError
try:
    print(math.PI)
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# KeyError
try:
    student = {"first_name": "Rayan"}
    print(student["last_name"])
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# TypeError
try:
    print(8 + "8")
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# ImportError
try:
    from math import power
except Exception as e:
    print(f"{type(e).__name__} : {e}")


# ValueError
try:
    int("12y")
except Exception as e:
    print(f"{type(e).__name__} : {e}")

# ZeroDivisionError
try:
    print(8 / 0)
except Exception as e:
    print(f"{type(e).__name__} : {e}")
