# CHANNEL : @Esfelurm | Github.com/esfelurm



import os
from time import sleep
try:import requests
except:os.system("pip install requests")
try:os.system("cls")
except:os.system("clear")
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
def APIS_PROXY(PROX,Name_File,Save):
	if PROX == "1":
		f = open(Name_File,'wb')
		SOCKS4 = [			
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
			"https://openproxylist.xyz/socks4.txt",
			"https://proxyspace.pro/socks4.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
			"https://www.proxy-list.download/api/v1/get?type=socks4",
			"https://www.proxyscan.io/download?type=socks4",
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
			"https://api.openproxylist.xyz/socks4.txt",
		]
		for api in SOCKS4:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}SOCKS4 : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()
		try:
			r = requests.get("https://www.socks-proxy.net/",timeout=5)
			Tag_H = str(r.content)
			Tag_H = Tag_H.split("<tbody>")
			Tag_H = Tag_H[1].split("</tbody>")
			Tag_H = Tag_H[0].split("<tr><td>")
			proxies = ""
			for proxy in Tag_H:
				proxy = proxy.split("</td><td>")
				try:
					proxies=proxies + proxy[0] + ":" + proxy[1] + "\n"
				except:
					pass
				fd = open(Name_File,"a")
				fd.write(proxies)
				fd.close()
		except:
			pass
	if PROX == "2":
		f = open(Name_File,'wb')
		SOCKS5 = [
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
			"https://www.proxy-list.download/api/v1/get?type=socks5",
			"https://www.proxyscan.io/download?type=socks5",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
			"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
			"https://api.openproxylist.xyz/socks5.txt",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5",
			"https://openproxylist.xyz/socks5.txt",
			"https://proxyspace.pro/socks5.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
		]
		for api in SOCKS5:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}SOCKS5 : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()
	if PROX == "3":
		f = open(Name_File,'wb')
		HTTP = [
			"https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
			"https://www.proxy-list.download/api/v1/get?type=http",
			"https://www.proxyscan.io/download?type=http",
			"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
			"https://api.openproxylist.xyz/http.txt",
			"https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
			"http://alexa.lr2b.com/proxylist.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
			"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
			"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
			"https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
			"https://proxy-spider.com/api/proxies.example.txt",
			"https://multiproxy.org/txt_all/proxy.txt",
			"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
			"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
			"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
			"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
			"https://openproxylist.xyz/http.txt",
			"https://proxyspace.pro/http.txt",
			"https://proxyspace.pro/https.txt",
			"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
			"https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
			"https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
			"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
			"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
			"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
			"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
			"https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
			"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
			"https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt",
			"https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
			"https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
			"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
			"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
			"https://rootjazz.com/proxies/proxies.txt",
			"https://sheesh.rip/http.txt",
			"https://www.proxy-list.download/api/v1/get?type=https",
		]
		for api in HTTP:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}HTTP : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()
	
	if PROX == "4":
		f = open(Name_File,'wb')
		HTTPS = ["https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
]
		for api in HTTPS:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}HTTPS : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()

	if PROX == "5":
		f = open(Name_File,'wb')
		Config = [
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub1.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub2.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub3.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub4.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub5.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub6.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub7.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Sub8.txt",
    "https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vmess.txt"
]
		for api in Config:
			try:
				r = requests.get(api,timeout=5)				
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}Config : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()

	if PROX == "6":
		f = open(Name_File,'wb')
		ShadowSocks = ["https://raw.githubusercontent.com/Bardiafa/Free-V2ray-Config/main/Splitted-By-Protocol/vless.txt","https://raw.githubusercontent.com/freefq/free/master/v2","https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub","https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/v2ray.config.txt"]
		for api in ShadowSocks:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}Vless : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()
	if PROX == "7":
		f = open(Name_File,'wb')
		Vless = ["https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all"]
		for api in Vless:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}Trojan/SS : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()

	if PROX == "8":
		f = open(Name_File,'wb')
		Vless = ["https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt"]
		for api in Vless:
			try:
				r = requests.get(api,timeout=5)
				if Save == "y" or Save == "Y":
					for Line in r.text.split('\n'):
						sleep(0.5)
						print (f"{lrd}[{lgn}+{lrd}] {lgn}Random : {gn}{Line}\n\n")
				else:f.write(r.content)
			except:
				pass
		f.close()
																		
	print("\n\nHave already downloaded proxies list as "+Name_File)
	print (f"\n\n {yw}thank you{lrd} | {gn}channel Telegram :{lgn} @Esfelurm {lrd}| ")

print (f"""
{yw}Written by {lrd}: {lgn}Hydra {yw}&& {lgn}Esfelurm {yw}| {gn}Version{lrd} : {lgn}2.0.1\n\n
{lrd}    ____       {lgn} ____
{lrd}   / __ \      {lgn}/ __ \_________  _  ____  __
{lrd}  / / / /{rd}_____{lgn}/ /_/ / ___/ __ \| |/_/ / / /
{lrd} / /_/ /{rd}_____{lgn}/ ____/ /  / /_/ />  </ /_/ /{lgn}
{lrd}/_____/{lgn}     /_/   /_/   \____/_/|_|\__, /
                                  /____/
""")
print (f"""
    {rd}| {gn}Socks4 {lrd}[{lgn}1{lrd}] {yw}-- {gn}Socks5 {lrd}[{lgn}2{lrd}] {yw}-- {gn}Http {lrd}[{lgn}3{lrd}]{yw} -- {gn}Https {lrd}[{lgn}4{lrd}] {yw}{rd}|
\n{rd}    | {gn}Config {lrd}[{lgn}5{lrd}] {yw}-- {gn}Vless  {lrd}[{lgn}6{lrd}] {yw}-- {gn}TrSe {lrd}[{lgn}7{lrd}] {yw}-- {gn}RDM   {lrd}[{lgn}8{lrd}] {rd}|""")

proxy = input(f"\n{lrd}[{lgn}?{lrd}] {yw}Enter protocol : {cn}")
Name_File = input(f"\n{lrd}[{lgn}+{lrd}] {cn}Please enter the path and name of the file you want the proxies to be saved in : ")
Save = input(f"\n{lrd}[{lgn}+{lrd}] {cn}Do you want to see the config/proxies in the terminal? [Y/N]")
APIS_PROXY(proxy,Name_File,Save)
