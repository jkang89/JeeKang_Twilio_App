# Jee's Derp Dogs Twilio App

The purpose of this app is to send a text daily every morning so that I wake up to a happy text of derpy dogs from the Reddit, r/WhatsWrongWithYourDog. I wake up to a lot of work related e-mails or other e-mails, and it's always a happier day when waking up to derpy dogs.

## Process of Development

There are three parts to this app:

1. Scrape the subreddit page r/WhatsWrongWithYourDog to pull the top three posts.
2. Use Twilio text messaging to send the top three posts to a phone number of your choice.
3. Deploy to Heroku to automate the running of the script.

## Deployment Difficulties

One of the biggest difficulties that I ran into was that the Twilio module wasn't recognized by Python 3 when attempting to use this [template](https://github.com/michaelkrukov/heroku-python-script?fbclid=IwAR3fyuwLVi1JmF9NvWJZBRCcyZIGea5AzjBumPtbI9XieluJ2Bgtj1_l-Bs) to deploy to Heroku. I wasn't able to find any solutions.

