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
pattern = r"[A-Za-z]+"

words = re.findall(pattern, paragraph)

count_word = {}

for word in words:
    if word.lower() in count_word:
        count_word[word.lower()] += 1
    else:
        count_word[word.lower()] = 1

list_word = [(v, k) for k, v in count_word.items()]

list_word.sort(key=lambda x: x[0], reverse=True)

print(list_word)

print("\nCheck variable name")


def check_var_value(txt):
    var_pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'

    check_var = re.match(var_pattern, txt)

    if check_var:
        return True
    else:
        return False


print(check_var_value("1first_name"))

print("Clean text")

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. 
There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;
I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

patter = r'[%#$&@;!]'

sentence = re.sub(patter, "", sentence)

print(sentence)