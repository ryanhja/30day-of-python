import requests

print("Romeo and Juliet API")
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response_rj = requests.get(romeo_and_juliet)

print("Cats API")
cats_api = 'https://api.thecatapi.com/v1/breeds'
response_ca = requests.get(cats_api)

weights = [w["weight"]["metric"] for w in response_ca.json()]

print(weights)
