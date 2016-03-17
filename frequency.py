import json
import sys

def main():
    input_file = open(sys.argv[1])
    total = 0
    dict_frequency = {}

    for line in input_file:
        for word in json.loads(line).text:
            dict_frequency[word] += 1
            total += 1

    for key in dict_frequency:
        dict_frequency[key] /= total
