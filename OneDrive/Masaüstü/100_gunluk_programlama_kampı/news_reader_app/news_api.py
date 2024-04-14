import tkinter
from tkinter import *
from tkinter import messagebox
import requests
import json

hbr = "https://api.collectapi.com/news/getNews?country=tr&tag=general"

headers = {'content-type': "application/json",
           'authorization': "apikey 2xA0m7VKqhos2lJeMgwhTP:0L7q1a6Ipc04hOUd6ZeZAZ"}

hbr_response = requests.get(url=hbr, headers=headers)
data = hbr_response.json()
result = data.get('result')

a = 1
for haber in result:
    h_adi = print("Haberin        Adı :", "No :", a, "=>", haber['name'])
    h_ack = print("Haberin Açıklaması :", "No :", a, "=>", haber['description'])
    h_kyn = print("Haberin    Kaynağı :", "No :", a, "=>", haber['source'])
    h_imj = print("Haberin      İmajı :", "No :", a, "=>", haber['image'])
    h_lnk = print("Haberin      Linki :", "No :", a, "=>", haber['url'])
    a+=1

haber_adi = tkinter.Label(text=h_adi).pack()
haber_aciklamasi = tkinter.Label(text=h_ack).pack()
haber_kaynagi = tkinter.Label(text=h_kyn).pack()
haber_imaji = tkinter.Label(text=h_imj).pack()
haber_linki = tkinter.Label(text=h_lnk).pack()