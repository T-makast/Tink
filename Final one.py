import re
import pickle

FILE_NAME = 'data.txt'


def text_process(dataCl):
    data = []
    for line in dataCl:
        data.append(text_cleaner(line))
    data = list(filter(None, data))
    return data


def text_cleaner(text):
    newString = text.lower()
    newString = re.sub(r"'s\b", "", newString)
    newString = re.sub("[^а-яА-Я]", " ", newString)
    newString = re.sub(" +", " ", newString)
    return "<s " + newString.strip() + " /s>"


def bigram_trans(strEx):
    # using zip() + split() + list comprehension
    return [i for j in strEx
            for i in zip(j.split(" ")[:-1], j.split(" ")[1:])]


df = open(FILE_NAME, 'r')
data_example = df.readlines()
print(bigram_trans(text_process(data_example)))

pickle_out = open("model.pickle", "wb")
pickle.dump(list, pickle_out)
pickle_out.close()
