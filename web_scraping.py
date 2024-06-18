import time
import sys
from bs4 import BeautifulSoup 
import requests 

try:
    page=requests.get('https://www.who.int/data/gho/data/themes/air-pollution/who-air-quality-database/2022')
except Exception as e:
    print(e)

time.sleep(2)
soup=BeautifulSoup(page.text,'html.parser')
link=soup.find_all('div',attrs={'class':'arrowed-link'})
print(page)
print(link[0].a)