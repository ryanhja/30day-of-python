# Day 19: 30 Days of python programming

import re

file_path = r'./obama_speech.txt'

with open(file_path, "r", encoding="utf-8") as f:
    obama_speech = f.readlines()
    print(f"Number of lines : {len(obama_speech)}")

    word = 0
    for row in obama_speech:
        for w in row:
            word += 1

    print(obama_speech)

    print(f"Number of words : {word}")
