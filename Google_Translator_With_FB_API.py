# You are free to Modify/Share this code.
# We would love to hear your feedback on this.
# firesofmay@gmail.com - github.com/firesofmay
# grvmjain@gmail.com - github.com/gmjain
# Enjoy

from BeautifulSoup import BeautifulSoup
import requests
import sys
import fbconsole

#Example input to enter : en (= english)
convert_from = raw_input("Language to Convert from : ")

#Example input to enter : hi (= hindi), fr (= french), de (= German)
convert_to = raw_input("Language to Convert to : ")

#Example input to enter : Hello World
text_to_convert = raw_input("Text to Convert : ")

#A url cannot have spaces as parameters, so we replace all the spaces with '+'
text_to_convert = text_to_convert.replace(' ', '+')

#Passing the parameters. This url you get via LiveHTTPHeader Firefox Plugin. Experiment with it, its easy.
url = 'http://translate.google.com/?sl=%s&tl=%s&text=%s' % (convert_from, convert_to, text_to_convert)

#Get the content
data = requests.get(url).content

#If you do this, it does not convert the elements properly.
#soup = BeautifulSoup(data)

#For unicode support use this.
soup = BeautifulSoup(data, convertEntities=BeautifulSoup.HTML_ENTITIES)
#soup = BeautifulSoup(data)

#Getting the result which is in div gt-res-content and inside that its in span result_box's text. Use Firebug to check this.
div_content = soup.find('div', {'id' : 'gt-res-content'})
converted_text = div_content.find('span', {'id':'result_box'}).text

#Awesomeness of Scraping!! woot woot :D /\
print "Converted Text : " + converted_text


#All the bloody Permissions I can get :p lol, and even the cookie doesn't expire soon ;)
fbconsole.AUTH_SCOPE = [ 'user_about_me',  'friends_about_me',  'user_activities',  'friends_activities',  'user_birthday',  'friends_birthday',  'user_checkins',  'friends_checkins',  'user_education_history',  'friends_education_history',  'user_events',  'friends_events',  'user_groups',  'friends_groups',  'user_hometown',  'friends_hometown',  'user_interests',  'friends_interests',  'user_likes',  'friends_likes',  'user_location',  'friends_location',  'user_notes',  'friends_notes',  'user_online_presence',  'friends_online_presence',  'user_photo_video_tags',  'friends_photo_video_tags',  'user_photos',  'friends_photos',  'user_questions',  'friends_questions',  'user_relationships',  'friends_relationships',  'user_relationship_details',  'friends_relationship_details',  'user_religion_politics',  'friends_religion_politics',  'user_status',  'friends_status',  'user_videos',  'friends_videos',  'user_website',  'friends_website',  'user_work_history',  'friends_work_history',  'email', 'read_friendlists',  'read_insights',  'read_mailbox',  'read_requests',  'read_stream',  'xmpp_login',  'ads_management',  'create_event',  'manage_friendlists',  'manage_notifications',  'offline_access',  'publish_checkins',  'publish_stream',  'rsvp_event',  'sms',  'publish_actions']
fbconsole.authenticate()

status = fbconsole.post('/me/feed', {'message':converted_text})
