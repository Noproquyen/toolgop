import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
#đánh dấu bản quyền
ndp_tool="\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
#Config
__SHOP__ = 'manhquyen.tk'
__ZALO__ = '0983779510'
__ADMIN__ = 'Mạnh Quyền'
__FACEBOOK__ = 'manhquyen10112004'
__VERSION__ = '1.0'
def banner():
 banner = f"""
\033[1;34m  █████╗ ███╗   ██╗     ██████╗ ██████╗ ██╗███╗   ██╗
\033[1;37m ██╔══██╗████╗  ██║    ██╔═══██╗██╔══██╗██║████╗  ██║
\033[1;34m ███████║██╔██╗ ██║    ██║   ██║██████╔╝██║██╔██╗ ██║
\033[1;37m ██╔══██║██║╚██╗██║    ██║   ██║██╔══██╗██║██║╚██╗██║
\033[1;34m ██║  ██║██║ ╚████║    ╚██████╔╝██║  ██║██║██║ ╚████║
\033[1;37m ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mTOOL GỘP PYTHON 1.0
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;36mMạnh Quyền
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;36mFB: \033[1;31mManhquyen10112004
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mZALO: \033[1;37mhttps://zalo.me/0983779510
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;34mWEB: \033[1;37mhttps://manhquyen.tk
\033[1;31m────────────────────────────────────────────────────────────
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
import json,requests,time
from time import strftime
print('Tool By Lê Mạnh Quyền')
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Trao Đổi Sub  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool TDS Profile ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool TDS Profile \033[1;31m[\033[1;33mV1\033[1;31m] ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool TDS FB ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool Auto TDS FB ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m5\033[1;31m] \033[1;32mTool TDS Tiktok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m66\033[1;31m] \033[1;32mTool TDS Now ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m6\033[1;31m] \033[1;32mTool TDS IG ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═══════════════════════╗")
print("\033[1;37m║  \033[1;33mTool Tương Tác Chéo  \033[1;37m║")
print("\033[1;37m╚═══════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m7\033[1;31m] \033[1;32mTool TTC TikTok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m8\033[1;31m] \033[1;32mTool TTC Token ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m9\033[1;31m] \033[1;32mTool TTC Profile ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTiện Ích Facebook  \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m10\033[1;31m] \033[1;32mTool Spam Message ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m11\033[1;31m] \033[1;32mTool Get Token FB ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m12\033[1;31m] \033[1;32mTool Reg Page Vị Trí ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33mTool PROFILE       \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m13\033[1;31m] \033[1;32mTool Buff View Story Max Speed Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m14\033[1;31m] \033[1;32mTool Reg Page Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m15\033[1;31m] \033[1;32mTool Get Token Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m16\033[1;31m] \033[1;32mTool Menber Group Pro5 ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m17\033[1;31m] \033[1;32mTool Share Ảo Pro5 ")
print("\033[1;31m────────────────────────────────────────────────────────────")
chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/a500b829-0087-4a8f-b3f6-101ebb79ecf7').text)
if chon == 2 :
	exec(requests.get('https://run.mocky.io/v3/5a3644c0-e217-4e49-a8cf-9d74f6552b1d').text)
if chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/8b1c1152-aff3-4f40-a3a8-f8a92ab4acfa').text)
if chon == 4 :
	exec(requests.get('https://run.mocky.io/v3/929d0ec1-24fb-403f-a7a6-5b625188ded0').text)
if chon == 5 :
	exec(requests.get('https://run.mocky.io/v3/c4633955-13ec-4707-a36e-52a6c926427e').text)
elif chon == 66 :
 exec(requests.get('https://run.mocky.io/v3/80dfe67c-6073-4839-996e-2496172a63a0').text)
if chon == 6 :
	exec(requests.get('https://run.mocky.io/v3/4da6d01f-62ba-4836-b9b2-64d79f472fc0').text)
if chon == 7 :
	exec(requests.get('https://run.mocky.io/v3/ef6729a1-1548-48cf-ab14-363208f48b59').text)
if chon == 8 :
	exec(requests.get('https://run.mocky.io/v3/3a6ec16a-3f13-478a-a400-69622182a268').text)
if chon == 9 :
	exec(requests.get('https://run.mocky.io/v3/e6235911-8862-43cc-9561-ed7453b9aadb').text)
if chon == 10 :
	exec(requests.get('https://run.mocky.io/v3/fca278a6-c1b8-40df-a35a-2115a45e2781').text)
if chon == 11 :
	exec(requests.get('https://run.mocky.io/v3/d38cfa2b-28ab-44ff-8ede-813898ff941f').text)
if chon == 12 :
	exec(requests.get('https://run.mocky.io/v3/91bcc211-369d-4c2c-9e89-650e1e9271ad').text)
elif chon == 13 :
	exec(requests.get('https://run.mocky.io/v3/3a6ec16a-3f13-478a-a400-69622182a268').text)
elif chon == 14 :
	exec(requests.get('https://run.mocky.io/v3/4b6ca251-283b-4d49-85e9-cd0a731485ec').text)
elif chon == 15 :
	exec(requests.get('https://run.mocky.io/v3/7c0b1444-8685-4a33-98c8-18713bca2211').text)
elif chon == 16 :
 exec(requests.get('https://run.mocky.io/v3/94c0852d-7373-474f-ae39-b2dd2b8d78aa').text)
elif chon == 17 :
 exec(requests.get('https://run.mocky.io/v3/1e0c4843-6aa2-4af0-8955-55fe1e1c4d34').text)
else :
	print (" Sai Lựa Chọn ")
	exit()