import requests
from BeautifulSoup import BeautifulSoup
import re
import urllib2

#Init Dictionary
kwargs = {}

#Populate the headers in the dictionary
kwargs['headers'] = {'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}

#Example
# input               = cisco-ios country:IN HTTP/1.0 200 OK
# replace (" ", "+")  = cisco-ios+country:IN+HTTP/1.0+200+OK
# unquoted            = cisco-ios+country:IN+HTTP/1.0+200+OK
# quoted              = cisco-ios+country%3AIN+HTTP%2F1.0+200+OK

query = raw_input("Query : ")
query = urllib2.quote(query)
query = query.replace(' ', '+')

#Above in one line :-
#query = urllib2.quote(raw_input("Query : ")).replace(' ', '+')

#Final URL to scrape
url = 'http://www.shodanhq.com/search?q=%s' % (query)

#Get the url contents in data
data = requests.get(url, **kwargs).content

#Get the Soup
soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

#Find all the div tags containing the result of the search
div_result = soup.findAll('div', 'result')

#Total Number of pages:
print re.sub(r'[^0-9\.]', '',((soup.findAll('a', 'pager_link'))[-2].text))

#Print each ip and its country
for each in div_result:
    
    #Find the ip in each result
    ip = each.find('div', {'class':'ip'})

    #The img tag has country info
    country = each.find('img')

    #Extract the ip address from the div tag
    print re.sub(r'[^0-9\.]', '',ip.text) + "\t",

    #Print the title field in img tag. title has the country name
    print country['title']
