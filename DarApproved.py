import time
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
    try:
        print("Running DarApproved...")
        tweets = api.user_timeline("Darunia18")
        for twt in reversed(tweets):
            if twt.id > int(last):
                try:
                    user_displayname = twt.retweeted_status.user.screen_name
                    tweet_id = twt.retweeted_status.id_str
                    api.update_with_media("DarApproved.png","@Darunia18 http://twitter.com/"+user_displayname+"/status/"+tweet_id)
                except:
                    if twt.in_reply_to_user_id_str is not None:
                        user_displayname = twt.in_reply_to_user_id_str
                        api.update_with_media("DarApproved.png","@Darunia18",in_reply_to_status_id=twt.id)
                    else:
                        api.update_with_media("DarApproved.png","@Darunia18",in_reply_to_status_id=twt.id)
                print(twt.text)
                last = twt.id
                file = open("last.txt",'w')
                file.write(str(last))
                file.close()
                print("Approved! Waiting for Darunia18 to tweet again.")
    except:
        print("An error occurred! Trying again soon!")
    print("Sleeping...")
    time.sleep(36)
