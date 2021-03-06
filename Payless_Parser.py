# You are free to Modify/Share this code.
# We would love to hear your feedback on this.
# firesofmay@gmail.com - github.com/firesofmay
# grvmjain@gmail.com - github.com/gmjain
# Enjoy


#requests is an awesome library replacement for httplib etc
#you need to install this
import requests

#BeautifulSoup is a html parser = \m/
#you need to install this
from BeautifulSoup import BeautifulSoup

#regular expression library for python
#inbuilt
import re


#Dictionary for User agents
kwargs = {}
kwargs['headers'] = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

#Url we'll be fecthing
url = 'http://www.payless.com/store/product/detail.jsp?catId=cat10243&subCatId=cat10243&skuId=091151050&productId=68423&lotId=091151&category='

#Calling the request library to fetch the url using the User Agent and give us the HTML Content and store it in data library
data = requests.get(url, **kwargs).content

#We convert that HTML data into a BeautifulSoup Object
soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

#We want to get the price, if it has a sale price, we want the sale price otherwise the standard price
#price is inside price-info div id which we checked by firebug firefox plugin
div_price = soup.find('div', {'id' : 'price-info'})

#inside the div_price we want to check if it has a sale price
sale_price = div_price.find('span', {'id' : 'saleprice'})

#if sale price is found get the sale price, else the normal price
if sale_price:

    #the .text part extracts the price out of that div
    #re.sub substitutes the given 3rd parameter - sale_price.text, matches the first 1st parameter (Regex here) and replaces it with second parameter (Which is nothing)
    #So basically re.sub will remove anything but the digits and a "." i.e. except for the price substitute everything with ""
    finalprice =  re.sub(r'[^0-9\.]', '',sale_price.text)
else:
    finalprice =  re.sub(r'[^0-9\.]', '',div_price.text)

#And you print the price
print "Price of this item is " + finalprice
