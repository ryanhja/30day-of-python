# Day 19: 30 Days of python programming

import re
import json


def file_description(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        print(f"File : {file_name}")
        txt = f.readlines()
        words = " ".join(txt)

        print(f"Number of lines : {len(txt)}")
        print(f"NUmber of words : {len(words.split())}\n")


# obama_speech.txt
file_description('obama_speech.txt')

# michelle_obama_speech.txt
file_description('michelle_obama_speech.txt')

# donald_speech.txt
file_description('donald_speech.txt')

# melina_trump_speech.txt
file_description('melina_trump_speech.txt')


# countries_data.json
with open('countries_data.json', 'r') as f:
    countries_json = json.loads(f.read())

    countries = [country for country in countries_json]

    print(type(countries))
