# You are free to Modify/Share this code.
# We would love to hear your feedback on this.
# firesofmay@gmail.com - github.com/firesofmay
# grvmjain@gmail.com - github.com/gmjain
# Enjoy

import requests
url = 'http://en.wikipedia.org/wiki/Python_%28programming_language%29'
data = requests.get(url).content
f = open("debug.html", 'w')
f.write(data)
f.close()
