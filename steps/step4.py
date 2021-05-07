#Recommending the Best Match
import json 
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys())) > 0:
        return "Did you mean %s instead?" %get_close_matches(w, data.keys())[0]    
    else:
        return "The word you want meaning does not exist. pleae double check it."   

word = input("Enter the word you want meaning of: ")   

print(translate(word))
