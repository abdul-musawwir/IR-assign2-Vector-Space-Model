import collections
import json
from nltk.stem import PorterStemmer
import math




def cleaner2(uncleaned):
    for x in range(len(uncleaned)):
        if ord(uncleaned[x]) < 97 or ord(uncleaned[x]) > 122:
            uncleaned =  uncleaned.replace(uncleaned[x],' ')
    return uncleaned

def cleaner(uncleaned):
    porter = PorterStemmer()
    uncleaned = uncleaned.lower()
    uncleaned = uncleaned.strip()
    uncleaned = uncleaned.translate({ord(i): None for i in '!\\@#-_:$%^&*();.,?/1”2’3“4‘567890\'\"'})
    for i in uncleaned:
        t = ord(i)
        if t < 97 or t>122:
            uncleaned = uncleaned.replace(i, "")
    uncleaned = porter.stem(uncleaned)
    return uncleaned
    #print(uncleaned)
    # for character in uncleaned:
    #     # print(character)
    #     if 90 >= character >= 65:
    #         character = character + 32
    #     if 97 > character > 122:
    #         character.

def fileRead(lexicon):
    folder = "./ShortStories/"
    ext = ".txt"

    for i in range(1,51):
        curr = str(i)
        #print(folder+curr+ext)
        with open(folder+curr+ext,'r',encoding='utf-8') as file:
            # reading each line    
            for line in file:
        
                # reading each word        
                for word in line.split():
                    word = word.strip()
                    if(len(word)!=0):
                        data = cleaner(word)
                        # print(data)
                        if data in lexicon:
                            if curr in lexicon[data]:
                                lexicon[data][i] += 1
                            else:
                                lexicon[data][i] = 1
                        else:
                            lexicon[data] = {}
                            if curr in lexicon[data]:
                                lexicon[data][i] += 1
                            else:
                                lexicon[data][i] = 1
                    # displaying the words           
                    # print(word)
    lexicon = collections.OrderedDict(sorted(lexicon.items()))
    # print(lexicon)
    # for keys,values in lexicon.items():
    #     print(keys)
    #     print(values)

    print(len(lexicon))
    # with open("lexicon.json", "w") as outfile: 
    #     json.dump(lexicon, outfile)
    return lexicon


def make_idf(lexicon):
    idf = dict()
    N = 50
    for term,docs in lexicon.items():
        df = len(docs)
        temp = math.log(N / df)
        idf[term] = temp
    return idf

def init_tf_idf_lexicon(lexicon):
    tf_idf = dict()
    for keys,values in lexicon.items():
        tf_idf[keys] = {}
        for leg in range(0,51):
            tf_idf[keys][leg] = float(0)
    return tf_idf

def tf_idf_lexicon(lexicon,idf):
    tf_idf = init_tf_idf_lexicon(lexicon)
    for term,docs in lexicon.items():
        for docNo,tf in docs.items():
            tf_idf[term][docNo] = tf * idf[term]

    return tf_idf
    # print(tf_idf)
    # print(idf)
    # for 
    # print(tf_idf)


def init_v_table():
    vector_table = dict()

    for i in range(0,51):
        vector_table[i] = {}
    return vector_table

def make_vector_table(tf_idf):
    vector_table = init_v_table()

    for terms, docs in tf_idf.items():
        for docNo, idf_tf in docs.items():
            vector_table[docNo][terms] = idf_tf

    return vector_table


def preprocessing():
    print("hello")
    lexicon = dict()
    lexicon = fileRead(lexicon)
    idf = make_idf(lexicon)
    tf_idf = tf_idf_lexicon(lexicon,idf)
    vector_table = make_vector_table(tf_idf)
    
    with open("lexicon.json", "w") as outfile: 
        json.dump(lexicon, outfile)

    with open("idf.json", "w") as outfile: 
        json.dump(idf, outfile)

    with open("tf_idf.json", "w") as outfile: 
        json.dump(tf_idf, outfile)
    
    with open("vector_table.json", "w") as outfile: 
        json.dump(vector_table, outfile)

    #cleaner("MATTTieuess!'wwe@@23")


preprocessing()