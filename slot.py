from bs4 import BeautifulSoup
import requests

#webscrapping for jumia


#we can define phones this way and in the future add the size of the RAM or ROm to the name
infinix_hot11 = {
    'name': 'infinix hot 11',
    'query': 'infinix+hot+11',
    'size': ('64gb' , '64 gb' , '64-gb')
}
page = 1
phones = []

# URL = f"https://slot.ng/category/smartphone-5.html?page={page}"
# slot = requests.get(URL)
# soup = BeautifulSoup(slot.text,'html.parser')

# print(soup.prettify())

while page <= 1:
    URL = f"https://slot.ng/category/smartphone-5.html?page={page}"
    slot = requests.get(URL)
    soup = BeautifulSoup(slot.text,'html.parser')
    print(soup.find_all(class_="Shared_cardbody__2YBh5"))
    for el in soup.find_all(class_="Shared_cardbody__2YBh5 p-2"):
        # phones.append(
        #     {
        #         'name':el.a.find(class_='name').get_text() ,
        #          'price':el.a.find(class_='prc').get_text() ,
        #           'link': el.a.get('href'),
        #           'img_src': el.a.find('img')['data-src']
        #           }
        #     )
        print(el)
    page+=1


# for phone in phones:
#     if infinix_hot11['name'].lower() in phone['name'].lower():
#         print(phone)
