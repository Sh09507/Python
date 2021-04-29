#sudo apt-get install python-pip -y
#python -m pip install beautifulsoup4

import urllib
import time
from bs4 import BeautifulSoup

# Open the URL and get the response
url = "https://thackston.me"
print("Opening " + url)
start = time.clock()
response = urllib.urlopen(url)
elapsed = time.clock() - start
print("Response code: " + str(response.getcode()))
print("Response time: " + str(elapsed))

# Check the status code and print results
if response.getcode() >= 200 and response.getcode() < 300:
	if response.geturl() != url:
		print("Redirected to " + response.geturl())
	html_doc = response.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	for link in soup.find_all('a'): # It helps to find all anchor tag's
		print(link.get('href'))
# Note: urllib.urlopen automatically follows redirects (codes 300-399)
elif response.getcode() >= 400 and response.getcode() < 500:
	print(str(response.getcode()) + " - Client error")
	html_doc = response.read()
	print(html_doc)
elif response.getcode() >= 500 and response.getcode() < 600:
	print(str(response.getcode()) + " - Server error")
	html_doc = response.read()
	print(html_doc)
else:
	print(str(response.getcode()))


