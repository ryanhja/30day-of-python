# Day 19: 30 Days of python programming

import re
import json


def file_description(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        print(f"File : {file_name}")
        txt = f.readlines()
        words = " ".join(txt)

        print(f"Number of lines : {len(txt)}")
        print(f"Number of words : {len(words.split())}\n")


# obama_speech.txt
file_description('obama_speech.txt')

# michelle_obama_speech.txt
file_description('michelle_obama_speech.txt')

# donald_speech.txt
file_description('donald_speech.txt')

# melina_trump_speech.txt
file_description('melina_trump_speech.txt')

print("Most spoken languages")


# Most spoken languages
def most_spoken_language(filename, limit):
    language_count = {}

    with open(filename, 'r') as f:
        countries_json = json.loads(f.read())

    for countries in countries_json:
        for country in countries["languages"]:
            if country.lower() in language_count:
                language_count[country.lower()] += 1

            else:
                language_count[country.lower()] = 1

    language_list = [(v, k.capitalize()) for k, v in language_count.items()]

    language_list.sort(key=lambda x: x[0], reverse=True)
    print(language_list[:limit])


most_spoken_language(filename='countries_data.json', limit=4)

print("\nMost populated countries")


# Most populated countries
def most_populated_country(filename, limit):
    with open(filename) as f:
        countries_json = json.loads(f.read())

    countries = [{'country': country["name"], 'population': country["population"]} for country in countries_json]
    countries.sort(key=lambda x: x["population"], reverse=True)

    print(countries[:limit])


most_populated_country(filename='countries_data.json', limit=4)

print("\nIncoming email addresses")


def extract_incoming_email_address(filename, limit):
    with open(filename) as f:
        txt_data = f.read()
        pattern = r'From: [A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}'
        matches = re.findall(pattern, txt_data)
        emails = []
        replace_pattern = "From: "
        for email in matches:
            emails.append(re.sub(replace_pattern, "", email))

        print(emails[:limit])


extract_incoming_email_address(filename='email_exchanges_big.txt', limit=4)

print("\nMost common words")
def find_most_common_words(filename, limit):
    with open(filename) as f:
        words = f.read().split()

        count_word = {}

        for wrd in words:
            if wrd.lower() in count_word:
                count_word[wrd.lower()] += 1
            else:
                count_word[wrd.lower()] = 1

        list_word = [(v, k) for k, v in count_word.items()]

        list_word.sort(key=lambda x:x[0], reverse=True)

        print(f"Speech : {filename}\n{list_word[:limit]}\n")

find_most_common_words(filename='sample.txt', limit=4)
find_most_common_words(filename='obama_speech.txt', limit=3)
find_most_common_words(filename='michelle_obama_speech.txt', limit=3)
find_most_common_words(filename='donald_speech.txt', limit=3)
find_most_common_words(filename='melina_trump_speech.txt', limit=3)