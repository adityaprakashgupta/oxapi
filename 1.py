import json
import requests
from main import getdata
with open('words_dictionary.json', 'r') as file:
    data = json.load(file)

print(type(data))

word_list = []
for i in data:
    deta = getdata(i)
    if deta['code'] == 200:
        word_list.append(deta)
    print(deta)


    with open('dict.json', 'w') as final:
        json.dump(word_list, final)
