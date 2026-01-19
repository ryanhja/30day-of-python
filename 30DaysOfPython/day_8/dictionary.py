# Day 6: 30 Days of python programming
dog = {}

print(dog)

dog["name"] = "Bobby"
dog["breed"] = "Pit Bull"
dog["age"] = 9

print(dog)

student = {
    "first_name": "",
    "last_name": "",
    "gender": "",
    "age": "",
    "skills": ["PYTHON", "JAVA"],
    "country": "",
    "city": "",
}

print(student)
print(len(student))
print(student["skills"])
print(type(student["skills"]))

new_skills = ["HTML", "CSS"]

student["skills"].extend(new_skills)

print(student)

student_key = student.keys()
print(student_key)

student_value = student.values()
print(student_value)

student_list = student.items()
print(student_list)

del student["HTML"]