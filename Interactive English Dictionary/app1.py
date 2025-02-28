import json
from difflib import get_close_matches
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
data_file_path = os.path.join(current_dir, "data.json")

dict_data = json.load(open(data_file_path))

def get_definition(word):
    word = word.lower()
    if word in dict_data:
        return dict_data[word]
    elif word.title() in dict_data:
        return dict_data[word.title()]
    elif word.upper() in dict_data:
        return dict_data[word.upper()]
    elif len(get_close_matches(word, dict_data.keys())) > 0:
        close_match = get_close_matches(word, dict_data.keys())[0]
        response = input(f"Did you mean {close_match}? Enter Y if yes, or N if no: ")
        if response.lower() == "y":
            return dict_data[close_match]
        elif response.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

while True:
    word = input("Enter a word('/x' to exit): ")
    if word == "/x":
        break
    output = get_definition(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)