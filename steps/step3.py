#Letter Case
import json 

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word you want meaning does not exist. pleae double check it."   

word = input("Enter the word you want meaning of: ")   

print(translate(word))