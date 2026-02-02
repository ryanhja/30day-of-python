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
