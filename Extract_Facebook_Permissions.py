# You are free to Modify/Share this code.
# We would love to hear your feedback on this.
# firesofmay@gmail.com - github.com/firesofmay
# grvmjain@gmail.com - github.com/gmjain
# Enjoy

#You need to have these Libraries Installed 
import requests
from BeautifulSoup import BeautifulSoup
import re

#We want to extract all the permissions from the first two tables, first two coloumns in a list.
data = requests.get('https://developers.facebook.com/docs/reference/api/permissions/').content

#Convert the data into a soup object
#We do convertEntities so that it converts a string with HTML entity codes (e.g. &lt; &amp;) to a normal string (e.g. < &)
soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)

#Find all the tables in the soup, convert them to string and make a list of all of them and store it in tables variable
tables = list(str(x) for x in soup.findAll('table'))

#Empty Perm_List variable
Perm_List = []

#Take only the first two tables, i.e. tables[0] and tables[1] only (as we are not interested in the other tables as of now)
for t in tables[:2]:

    #Convert the list object into a string by doing a join operation on it and make it a line string variable 
    line = "".join(t)

    #Extract all the permissions. All the permissions have <code> and </code> around them. () captures anything inside them. .* captures anything.
    #Therfore capture anything i.e. inside the code tags and add it to the Perm_List
    Perm_List += re.findall(r'<code>(.*)</code>', line)

#Done :)
print Perm_List
