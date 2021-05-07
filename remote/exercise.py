import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)


def translate(w):
    w = w.lower()
    if w in results:
        return results[w]
    elif w.title() in results:
        return results[w.title()]
    elif w.upper() in results:
        return results[w.upper()]        
    elif len(get_close_matches(w,results.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes N if no: " %get_close_matches(w, results.keys())[0])
        if yn == "Y":
            return results[get_close_matches(w, results.keys())[0]]
        elif yn == "N":
            return "The word you want meaning does not exist. pleae double check it."
        else:
            return "we didn't understand your entry"    
    else:
        return "The word you want meaning does not exist. pleae double check it." 

cursor = con.cursor()

word = input("Enter the word: ")

query = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)   