from bs4 import BeautifulSoup
import requests

#webscrapping for jumia


#we can define phones this way and in the future add the size of the RAM or ROm to the name
infinix_hot11 = {
    'name': 'infinix hot 11'
}

URL = "https://www.jumia.com.ng/smartphones/?page=1"
jumia = requests.get(URL)
soup = BeautifulSoup(jumia.text,'html.parser')
phones = []

for el in soup.find_all(class_="prd"):
    phones.append({'name':el.a.find(class_='name').get_text() , 'price':el.a.find(class_='prc').get_text()})

for phone in phones:
    if infinix_hot11['name'].lower() in phone['name'].lower():
        print(phone)