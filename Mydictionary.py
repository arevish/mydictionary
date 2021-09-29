from dictonaryword import words
from difflib import get_close_matches
# meaning = input("Please enter the word whose meaning you searching for: ").lower()
# print(meaning + ": " +words[meaning])

# valid_entry = input("Please enter the word whose meaning you searching for: ")
# print(": " + words[valid_entry])
data = words
def get_meaning(word):
    
    if word in data:
        if len(data[word])>1:
            for i in data[word]:
                print(i)
        else:
            print("data not found")
    else:
        close_match = get_close_matches(word, data.keys())
        if len(close_match)>0:
            print("finding the closest match to this is : ", close_match)
            print(close_match[0])
            for i in data[close_match[0]]:
                print( i)
        else:
            print("There is no word related to it, Can't found the word! ")
word = input("Please enter the word whose meaning you searching for: ").lower()
get_meaning(word)