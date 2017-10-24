import re
import requests



def extractfunction(myUrl='http://www.google.rs'):
    query = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    #url = 'http://facebook.com'
    url = myUrl
    while True:
        req = requests.get(url).text
        res = re.findall(query, req)
        dict = {}
        i = 0
        for r in res:
            i += 1
            dict[i] = r
        print()
        print(dict)
        my_choice = (int)(input())
        if my_choice == 0:
            print('back:',back)
            url = back
        else:
            back = url
            url = dict.get(my_choice)

def extractfunctionForGui(myUrl='http://www.google.rs'):
    query = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url = myUrl
    req = requests.get(url).text
    res = re.findall(query, req)
    dict = {}
    i = 0
    for r in res:
        i += 1
        dict[i] = r
    print()
    print(dict)
    return dict