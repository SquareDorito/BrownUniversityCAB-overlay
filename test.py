import urllib2
import requests
from bs4 import BeautifulSoup

url = raw_input("Enter a website to extract the URL's from: ")
r = requests.get("http://" +url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

for link in soup.find_all('p'):
    print(link.text)

#name_box=soup.find('p',attrs={'class':'title'})
#name=name_box.text

#print('Course Name: ',name)
#print('Review: ',content)
