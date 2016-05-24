import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

file = open("last.txt")
last = file.read()
file.close()
if last == '':
    last = '0'
while True:
    tweets = api.user_timeline("Darunia18")
    for twt in tweets:
        if twt.id > int(last):
            last = twt.id
            api.update_with_media("DarApproved.png","@Darunia18",in_reply_to_status_id=last)
            print(twt.text)
            file = open("last.txt",'w')
            file.write(str(last))
            file.close()
            print("Approved! Waiting for Darunia18 to tweet again.")
