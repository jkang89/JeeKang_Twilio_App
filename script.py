# Import from Twilio and Beautiful Soup
from twilio.rest import Client
import os

# Denote r/WhatsWrongWithYourDog as the page to scrape
# Use Beautiful Soup to grab top 3 titles and URLs from subreddit
# Integrate Twilio to send list of top 3 posts as text

account_sid = os.environ.get('TWILIO_SID') 
auth_token = os.environ.get('TWILIO_KEY') 
client = Client(account_sid, auth_token) 

body = 'Test'
 
message = client.messages.create( 
                              from_=os.environ.get('FROM_NUMBER'),        
                              to=os.environ.get('TO_NUMBER'),
                              body=body
                          ) 
 
print(message.sid)

# Deploy to Heroku and automate sending of text daily

