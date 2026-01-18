# Day 6: 30 Days of python programming

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")
print(it_companies)

it_companies.update(['Open AI', 'Grok', 'Github'])
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.discard("Open")
print(it_companies)

it_companies.remove("Google")
print(it_companies)

C = A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B))

print(A.symmetric_difference(B))

del A
del B

age_st = set(age)

print(age)
print(len(age))
print(age_st)
print(len(age_st))

text = "I am a teacher and I love to inspire and teach people"
lst_text = text.split(" ")
print(lst_text)
print(len(lst_text))

set_text = set(lst_text)
print(set_text)
print(len(set_text))