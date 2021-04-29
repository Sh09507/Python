#sudo apt-get install python-pip -y
#python -m pip install beautifulsoup4
#python -m pip install requests

import requests
import time
from bs4 import BeautifulSoup

def trylogin(payload, attempts):
    headers = {'User-Agent': 'Mozilla/5.0'}
    totaltime = 0
    for i in range(0,attempts):
        session = requests.Session()
        start = time.clock()
        response = session.post('https://russellthackston.me/index.php',headers=headers,data=payload)
        totaltime += time.clock() - start

        # Check for a successful login (Hint: look for New Topic form)
        html_doc = response.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        newtopicform = soup.find_all('form', {"action" : "newtopic.php"})
    return totaltime / 10

payload_good = {'username':'russell', 'password':'password10'}
payload_badpassword = {'username':'russell', 'password':'password10x'}
payload_badcredentials = {'username':'russellx', 'password':'password10x'}
attempts = 20

print("Average good login:            " + str(trylogin(payload_good, attempts)))
print("Average bad password:          " + str(trylogin(payload_badpassword, attempts)))
print("Average bad username/password: " + str(trylogin(payload_badcredentials, attempts)))
