#Returning the Definition of a Word
import json 

data = json.load(open("data.json"))

def translate(w):
    return data[w]

word = input("Enter the word: ")  

print(translate(word))