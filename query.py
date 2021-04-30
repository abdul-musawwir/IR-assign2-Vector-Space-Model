from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import json


def cleaner(uncleaned):
    porter = PorterStemmer()
    lemma = WordNetLemmatizer()
    uncleaned = uncleaned.lower()
    uncleaned = uncleaned.strip()
    uncleaned = uncleaned.translate({ord(i): None for i in '!\\@#-_:$%^&*();.,?/1”2’3“4‘567890\'\"'})
    for i in uncleaned:
        t = ord(i)
        if t < 97 or t>122:
            uncleaned = uncleaned.replace(i, "")
    # uncleaned = porter.stem(uncleaned)
    uncleaned = lemma.lemmatize(uncleaned)
    return uncleaned


with open('lexicon.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
# print(data)
print(len(data))
# with open("lexicon23.json", "w") as outfile: 
#     json.dump(data, outfile)

while True:
    query =  input()
    query = query.split(" ")

    for word in query:
        word = cleaner(word)
        # print ("hello")
        print(data[word])
    print(query)