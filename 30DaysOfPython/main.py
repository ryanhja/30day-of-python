# students = []
# for _ in range(2):
#     name = input("Name : ")
#     score = float(input("score : "))
#
#     students.append([name, score])

students = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39]
]

grades = sorted(list(set([x[1] for x in students])))
print(grades)
students.sort(key=lambda x: x[1])


second_lowest_score = students[1][1]

print(second_lowest_score)

execo_lowest = [student for student in students if student[1] == students[1][1]]
execo_lowest = sorted(execo_lowest, key=lambda x:x[0])
for student in execo_lowest:
    print(student[0])

