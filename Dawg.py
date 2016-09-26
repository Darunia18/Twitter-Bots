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
        print("Running Dawg...")
        tweets = api.user_timeline("account",count=200)
        for twt in reversed(tweets):
            if twt.id > int(last):
                last = twt.id
                file = open("backup.txt",'w')
                file.write(str(last))
                file.close()
                text = twt.text
                try:
                    retweeted_id = twt.retweeted_status.id_str
                    retweeted_user = twt.retweeted_status.user.screen_name
                    #api.retweet(retweeted_id)
                    api.update_status("Yo, http://twitter.com/"+retweeted_user+"/status/"+retweeted_id+" Dawg out. *drops mic*")
                    print(text)
                except:
                    if "Generic text" not in text:
                        if "Generic text 2" not in text:
                            if twt.in_reply_to_user_id_str is not None:
                                #This would be very annoying
                                pass
                            else:
                                # try:
                                #     lst = []
                                #     for media in status.entities['media']:
                                #         urlref= media['media_url_https']
                                #         lst.append(urlref)
                                #     urls = ' '
                                #     for i in lst:
                                #         urls = urls + ' '
                                #     api.update_status(text+urls)
                                # except:
                                #     api.update_status(text)
                                text = text.replace('@','')
                                text = text.replace('&amp;','&')
                                text = "Yo, "+text+" Dawg out. *drops mic*"
                                if len(text) > 140:
                                    one = '(1/2) '
                                    two = '(2/2) '
                                    words = text.split()
                                    split = False
                                    for word in words:
                                        if split is False:
                                            if len(one) + len(word) < 140:
                                                one = one + word + ' '
                                            else:
                                                two = two + word + ' '
                                                split = True
                                        else:
                                            two = two + word + ' '
                                    api.update_status(one)
                                    api.update_status(two)
                                    print(twt.text)
                                else:
                                    api.update_status(text)
                                    print(twt.text)
                file = open("last.txt",'w')
                file.write(str(last))
                file.close()
                print("Dawg'd. Waiting for Dawg to tweet again.")
                time.sleep(1)
    except:
        print("An error occurred! Trying again soon!")
    print("Sleeping...")
    time.sleep(36)
