from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from pattern3.en import singularize
import re
import json
import math

def cleaner(uncleaned):
    porter = PorterStemmer()
    lemma = WordNetLemmatizer()
    uncleaned = uncleaned.lower()
    uncleaned = singularize(uncleaned)
    uncleaned = re.sub(r'ly$', r'', uncleaned)
    uncleaned = re.sub(r'ed$', r'', uncleaned)
    uncleaned = re.sub(r'ing$', r'', uncleaned)
    uncleaned = re.sub(r'nes$', r'', uncleaned)
    # print(uncleaned)
    # uncleaned = uncleaned.strip()
    # uncleaned = uncleaned.translate({ord(i): None for i in '!\\@#-_:$%^&*();.,?/1”2’3“4‘567890\'\"'})
    # for i in uncleaned:
    #     t = ord(i)
    #     if t < 97 or t>122:
    #         uncleaned = uncleaned.replace(i, "")
    # uncleaned = lemma.lemmatize(uncleaned)
    # uncleaned = porter.stem(uncleaned)
    # print(uncleaned)
    return uncleaned

def read_query():
    query = str(input())
    # print(query)
    stop_word = []
    with open("Stopword-List.txt",'r') as stop:
        for line in stop:
            temp = line.strip()
            stop_word.append(temp)

    query = query.split(" ")
    # print(query)
    for i in range(len(query)):
        query[i] = cleaner(query[i])

    for word in query:
        if word in stop_word:
            query.remove(word)
    # print(query)
    return query

def insert_query_tf(vector_table,query):
    for term in query:
        vector_table['0'][term] += 1
    return vector_table

def idf_mul(vector_table,idf):
    for term,idf_val in idf.items():
        vector_table['0'][term] = vector_table['0'][term] * idf_val
    return vector_table

def cal_mag(vec):
    sum1 = 0
    for key,value in vec.items():
        temp = value*value
        sum1 += temp
    mag = math.sqrt(sum1)
    return mag

def calculate_sim(vector_table):
    
    query_mag = cal_mag(vector_table['0'])
    # print(query_mag)
    sim_table = {}
    
    for i in range(1,51):
        doc_mag = cal_mag(vector_table[str(i)])
        # print(doc_mag)
        sum2 = 0
        for term,value in vector_table['0'].items():
            if value != 0.0:
                sum2 = sum2 + (value * vector_table[str(i)][term])
        dot_prod = sum2
        # print(dot_prod)
        sim_table[i] = dot_prod / (query_mag * doc_mag)

    return sim_table

def my_filter(sim_table,alpha):
    result = []
    for docNo, sim in sim_table.items():
        if sim > alpha:
            result.append(docNo)
    return result

def queryprocessing():
    # with open('lexicon.json') as f:
    #     lexicon = json.load(f)

    with open('idf.json') as f:
        idf = json.load(f)

    # with open('tf_idf.json') as f:
    #     tf_idf = json.load(f)

    with open('vector_table.json') as f:
        vector_table = json.load(f)

    # print(lexicon)
    # print(idf)
    # print(tf_idf)
    # print(vector_table)
    query =""

    while True:
        query = read_query()
        if query[0] == "end":
            break

        vector_table = insert_query_tf(vector_table,query)
        vector_table = idf_mul(vector_table,idf)

        sim_table = calculate_sim(vector_table)

        alpha = 0.0015

        result = my_filter(sim_table, alpha)
        print(result)
        print(len(result))

    # print(sim_table)
    # print(vector_table['0'])

    

    #     # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    #     # print(data)
    #     # print(len(data))
    #     # with open("lexicon23.json", "w") as outfile: 
    #     #     json.dump(data, outfile)

    # while True:
    #     query =  input()
    #     query = query.split(" ")

    #     for word in query:
    #         word = cleaner(word)
    #         # print ("hello")
    #         print(data[word])
    #     print(query)

queryprocessing()