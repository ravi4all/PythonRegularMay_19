import bs4
import urllib.request as url

http = url.urlopen('https://www.flipkart.com/boat-rockerz-255f-bluetooth-headset-mic/p/itmf6tft2fkvgayj?pid=ACCF6SZ8EFWFEPZ6&lid=LSTACCF6SZ8EFWFEPZ6XLADSF&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_0_8&otracker1=AS_QueryStore_OrganicAutoSuggest_0_8&fm=SEARCH&iid=a69cf1f3-2fd3-40b7-bbca-0aa8a11cb2bb.ACCF6SZ8EFWFEPZ6.SEARCH&ppt=SearchPage&ppn=Search&ssid=fmeem9n8kg0000001558852249732&qH=55768db7281a5d52')
#print(http)

source = bs4.BeautifulSoup(http,'lxml')
span = source.find('span', class_='_35KyD6')
print(span.text)

price = source.find('div', class_='_3qQ9m1')
print(price.text)

items = source.findAll('li', class_='_2-riNZ')
for item in items:
    print(item.text)
