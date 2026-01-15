# Day 4: 30 Days of python programming

print("Exercise 01:")
str_1 = "Thirty"
str_2 = "Days"
str_3 = "Of"
str_4 = "Python"
space = " "
result_01 = str_1 + space + str_2 + space + str_3 + space + str_4
print(result_01)

print("\nExercise 02:")
result_02 =  'Coding' + ' ' + 'For' + ' ' + 'All'
print(result_02)

print("\nExercise 03:")
company = "Coding For All"

print("\nExercise 04:")
print(company)

print("\nExercise 05:")
print(len(company))

print("\nExercise 06:")
print(company.upper())

print("\nExercise 07:")
print(company.lower())

print("\nExercise 08:")
text = "Coding For All"

print("Capitalize : ",text.capitalize())
print("Title : ",text.title())
print("Swapcase : ",text.swapcase())

print("\nExercise 09:")
first_word = text.split(" ")[0]
print(first_word)

print("\nExercise 10:")
print("Index using Find : ", text.find("Coding"))
print("Index using Index : ",text.index("Coding"))

print("\nExercise 11:")
text = text.replace("Coding", "Python")
print("Replace text : ",text)

print("\nExercise 12:")
text = "Coding For All"
word = text.split(" ")
print("Split text  : ", word)

print("\nExercise 13:")
print("Index 0 of text : ", text[0])

print("\nExercise 14:")
print("Last index of text : ", text[-1])

print("\nExercise 15:")
text = "Python For Everyone"
abbr = ".".join([w[0] for w in text.split(" ")])

print("Text abbreviation 1 : ", abbr)

abbrs = ".".join([w for w in text if w.isupper()])
print("Text abbreviation 2  : ", abbrs)

print("\nExercise 16:")
text = '   Coding For All      '
print("Remove left, right space : ",text.strip(" "))

print("\nExercise 17:")
text_1 = "30DaysOfPython"
text_2 = "thirty_days_of_python"
print("Check identity : ", text_1.isidentifier())
print("Check identity : ", text_2.isidentifier())

print("\nExercise 18:")
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("Join list : ", " # ".join(python_libraries))

print("\nExercise 19:")
text = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(text)

print("\nExercise 20:")
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")