import requests
import numpy as np

print("Romeo and Juliet API")
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response_rj = requests.get(romeo_and_juliet)

print("Cats API")
cats_api = 'https://api.thecatapi.com/v1/breeds'
response_ca = requests.get(cats_api)

weights = [w["weight"]["metric"].split(" - ") for w in response_ca.json()]
metrics = [int(weight[1]) - int(weight[0]) for weight in weights]

min_metric= min(metrics)
max_metric= max(metrics)
median_metric= np.median(metrics)

print(min_metric)
print(max_metric)
print(median_metric)
