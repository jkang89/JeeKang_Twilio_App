# Import from Twilio and Beautiful Soup
from twilio.rest import Client
import os
import requests
import time
from bs4 import BeautifulSoup

# Denote r/WhatsWrongWithYourDog as the page to scrape
url = "https://old.reddit.com/r/WhatsWrongWithYourDog/"
# Use Beautiful Soup to grab top 3 titles and URLs from subreddit
headers = {'User-Agent': 'Mozilla/5.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')
domains = soup.find_all("div", {"class": "thing"})

body = "The top three links on /r/WhatsWrongWithYourDog: \n"

for i in range(1, 4):
	title = domains[i].find("p", class_="title").text
	href = domains[i].find("a")["href"]
	if href[0] == "/":
		href = "https://www.reddit.com" + href
	text = str(i) + ". " + title + " : " + href
	body += text + "\n"

# Integrate Twilio to send list of top 3 posts as text

account_sid = os.environ.get('TWILIO_SID') 
auth_token = os.environ.get('TWILIO_KEY') 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_=os.environ.get('FROM_NUMBER'),        
                              to=os.environ.get('TO_NUMBER'),
                              body=body
                          ) 
 
print(message.sid)

# Deploy to Heroku and automate sending of text daily

