from colorama import Fore as color
from time import sleep
from requests import get
from fuzzywuzzy import fuzz
from googlesearch import search
from bs4 import BeautifulSoup
bold = "\033[1m"
enbold = "\033[0m"



def banner():
    
    print(color.RED+"""
          /¸...¸`:·
      ¸.·´  ¸   `·.¸.·´)
     : © ):´;      ¸  {
      `·.¸ `·  ¸.·´\`·¸)
          `\\´´\¸.·´  """)
    sleep(0.3)
def banner2():
    print(color.RED+"""    

 ██▀███  ▓█████ ▓█████▄   █████▒ ██▓  ██████  ██░ ██ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▓██   ▒ ▓██▒▒██    ▒ ▓██░ ██▒
▓██ ░▄█ ▒▒███   ░██   █▌▒████ ░ ▒██▒░ ▓██▄   ▒██▀▀██░
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░▓█▒  ░ ░██░  ▒   ██▒░▓█ ░██ 
░██▓ ▒██▒░▒████▒░▒████▓ ░▒█░    ░██░▒██████▒▒░▓█▒░██▓
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒  ▒ ░    ░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒  ░       ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
  ░░   ░    ░    ░ ░  ░  ░ ░     ▒ ░░  ░  ░   ░  ░░ ░
                     <<<CHARON>>>         """)
banner()
banner2()
sleep(0.3)

print(bold+color.LIGHTBLUE_EX+"""         
    -------------------------
    | coder : CHARON        |
    | ID : @CHARON369       |
    | channel : @Norach369  |
    ------------------------- """+enbold)
sleep(0.2)


query   = input(color.BLACK + color.RED + 'HOSTNAME :  ' + color.RESET + color.WHITE)
results = 100

print(color.GREEN + '[*] start' + query)
for url in search(query, stop = results):
	print('\n' + color.CYAN + '[+] Url detected: ' + url)
	try:
		text = get(url, timeout = 1).text
	except:
		continue
	soup = BeautifulSoup(text, "html.parser")
	links_detected = []
	try:
		print(color.MAGENTA + '[?] Title: ' + soup.title.text.replace('\n', ''))
	except:
		print(color.RED + '[?] Title: null')
	try:
		for link in soup.findAll('a'):
			href = link['href']
			if not href in links_detected:
				if href.startswith('http'):
					if url.split('/')[2] in href:
						links_detected.append(href)
					elif query.lower() in href.lower():
						print(color.GREEN + '--- Requested data found at link : ' + href)
						links_detected.append(href)
					elif fuzz.ratio(link.text, href) >= 60:
						print(color.GREEN + '--- Text and link are similar : ' + href)
						links_detected.append(href)
	except:
		continue
	if links_detected == []:
		print(color.RED + '--- No data found')
