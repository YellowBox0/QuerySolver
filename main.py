import requests
import time
import datetime as dt
from pytz import timezone
from datetime import datetime
import json
import tkinter as tk
import tkinter.messagebox
import tkinter.constants as SUNKEN
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
 

user = input("What username you decide to use?\n")

print('1: Get the time & date in India.')

print('2: Get a random quote.')

print('3: Get the latest headlines From BBC News.')

print('4: Get the meaning of a word. (Args: <word>)')

print('5: Get a fact about a animal. (Args: <animal>)')

print('6: Get the lyrics of a song. (Args: <song>)')

print("\n")
time.sleep(2)
query = input('What is your query ( 1/2/3/4/5/6 ): ')

if query == "1":
    dt_India = dt.datetime.utcnow() + dt.timedelta(hours=5, minutes=30)
    Indian_time = dt_India.strftime('%d-%b-%y %H:%M:%S')
    UTC_time = dt.datetime.utcnow().strftime('%d-%b-%y %H:%M:%S')
    max_len = len(max(['UTC Time', 'Indian Time'], key=len))
    print(f"{'UTC Time'   :<{max_len}} - {UTC_time}")
    print(f"{'Indian Time':<{max_len}} - {Indian_time}")
    time.sleep(10)


if query == "2":
    r = requests.get('https://api.quotable.io/random')
    json = r.json()
    print("\n")
    print(json['content'])
    print("Author: " + json['author'])
    print("Character legnth (QUOTE): " + str(json['length']))
    time.sleep(10)

if query == "3":
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "d805f59c19c94083889eb38b76d17936"
    }

    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
    article = open_bbc_page["articles"]
	
    results = []

    for ar in article:
        results.append(ar["title"])
    for i in range(len(results)):
        print(i + 1, results[i])
        time.sleep(10)

if query == "4":
    word = input('Word: ')
    a = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    json = a.json()
    print('Meaning: ' + json[0]['meanings'][0]['definitions'][0]['definition'])
    time.sleep(10)


if query == "5":
    print('Bird / Cat / Dog / Fox / Koala / Panda')
    q = input('Which Animal: ')
    api = requests.get(f'https://some-random-api.ml/facts/{q}').json()
    print(api['fact'])
    time.sleep(10)
    if api['title'] == "No Definitions Found":
	    print('Invalid word!')


if query == "6":
    song = input('What is the song name: ')
    a = requests.get(
        f'https://some-random-api.ml/others/lyrics?title={song}').json()
    print(a['disclaimer'])
    time.sleep(3)
    print('Author:' + a['author'])
    time.sleep(2)
    print(a['lyrics'])
    time.sleep(10)
