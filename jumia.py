from bs4 import BeautifulSoup
import requests

#webscrapping for jumia


#we can define phones this way and in the future add the size of the RAM or ROm to the name
infinix_hot11 = {
    'name': 'infinix hot 11',
    'query': 'infinix+hot+11'
}
page = 1
phones = []

while page <= 2:
    URL = f"https://www.jumia.com.ng/smartphones/?q={infinix_hot11['query']}&sort=lowest-price&page={page}"
    jumia = requests.get(URL)
    soup = BeautifulSoup(jumia.text,'html.parser')
    for el in soup.find_all(class_="prd"):
        phones.append(
            {
                'name':el.a.find(class_='name').get_text() ,
                 'price':el.a.find(class_='prc').get_text() ,
                  'link': el.a.get('href'),
                  'img_src': el.a.find('img')['data-src']
                  }
            )
    page+=1


for phone in phones:
    if infinix_hot11['name'].lower() in phone['name'].lower():
        print(phone)
