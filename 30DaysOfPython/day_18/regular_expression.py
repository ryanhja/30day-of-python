# Day 18: 30 Days of python programming

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

print("\nMatch")
match = re.match("Python", txt, re.I)
print(match)

print("\nSearch")
match = re.search("python", txt, re.I)
print(match)

print("\nFind All")
match = re.findall("python", txt)
print(match)

print("\nReplace")
match_replace = re.sub("Python", "Javascript", txt, re.I)
print(match_replace)

print("\nPattern")
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for 12 a first programming language'''
pattern = r"Python | python"
matches = re.findall(pattern, txt)
print(matches)

print("\nMost frequent word")
paragraph = """I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."""
pattern = ""
