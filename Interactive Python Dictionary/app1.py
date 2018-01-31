# Interactive python dictionary that retrives information from JSON
# Show the output if exists 
# Also able to give suggestion from close words
# If doesnt exist ask for new word
import json
from difflib import get_close_matches  
# This module provides classes and functions for comparing sequences. It can be used for example, for comparing files, 
# and can produce difference information in various formats, including HTML and context and unified diffs.

data = json.load(open("data.json"))


def translate(w):
    w = w.lower() # .lower() was used to get all the lowercase matching from json
    if w in data:
        return data[w]
    elif w.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0: # so when the word is more than 1 or letter difflib module will provide suggestion
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
