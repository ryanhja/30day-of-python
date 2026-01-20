# Day 6: 30 Days of python programming
age = int(input("Enter your age : "))

if age >= 18:
    print ("You are old enough to learn to drive.")
else:
    print(f"You need { 18 - age } more years to learn to drive.")


my_age = 24
your_age = int(input("Enter your age : "))

if my_age > your_age and (my_age - your_age) == 1:
    print(f"You are {my_age - your_age} year young than me")
elif my_age > your_age and (my_age - your_age) != 1:
    print(f"You are {my_age - your_age} years young than me")
elif my_age < your_age and (your_age - my_age) == 1:
    print(f"You are {your_age - my_age} year old than me")
elif my_age < your_age and (your_age - my_age) != 1:
    print(f"You are {your_age - my_age} years old than me")


score = int(input("Enter your score : "))

if score >=90 :
    print("Your grade is A")
elif score >= 80 :
    print("Your grade is B")
elif score >= 70:
    print("Your grade is C")
elif score >= 60 :
    print("Your grade is D")
elif score < 60 :
    print("Your grade is F")