#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "pILfXhSpQAzfCnLycaTab3DbY"
consumer_secret = "ls8ZKd1VAnSnoPXEpRzLrCh6JmwpHM5Jquxaf2zVTSMyM9BnXB"
access_key = "1234696777971970048-QNZdgLSIwjVXZV8yW5csa75IqNLkVl"
access_secret = "7Ao0DYP4PKJwsOJclYsUwUPt1gaLUKMfPRRjlatObOcXn"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True, compression=True)

def get_neighbours(screenname):

	followee = []
	followers = []
	# for pg in tweepy.Cursor(api.followers, screen_name=screenname).items(100):
	# 	print(pg)
	# 	print("---------------------------")
	user_info = [[user.screen_name, user.followers_count, user.friends_count, user.statuses_count] for user in tweepy.Cursor(api.followers, screen_name=screenname).items(200)]
	print(len(user_info))
	#write the csv	
	with open('%s_followers.csv' % screenname, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["screen_name","followers","friends","total_tweets"])
		writer.writerows(user_info)
	
	followee_info = [[user.screen_name, user.followers_count, user.friends_count, user.statuses_count] for user in tweepy.Cursor(api.friends, screen_name=screenname).items(200)]
	print(len(followee_info))
	#write the csv	
	with open('%s_followees.csv' % screenname, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["screen_name","followers","friends","total_tweets"])
		writer.writerows(followee_info)
	
	pass

# 	print(len(followee))

# 	with open('%s_followees.csv' % screenname, 'w') as f:
# 		writer = csv.writer(f)
# 		writer.writerow(["followees"])
# 		writer.writerows(followee)

# 	print("Followers")

# 	for user in tweepy.Cursor(api.followers, screen_name=screenname, count = 10).items():
# 		followers.append(user.screen_name)

# 	print(len(followers))


# 	with open('%s_followers.csv' % screenname, 'w') as f:
# 		writer = csv.writer(f)
# 		writer.writerow(["followers"])
# 		writer.writerows(followers)


# #Below function could be used to make lookup requests for ids 100 at a time leading to 18K lookups in each 15 minute window
# def get_usernames(userids, api):
#     fullusers = []
#     u_count = len(userids)
#     print(u_count)
#     try:
#         for i in range(int(u_count/100) + 1):            
#             end_loc = min((i + 1) * 100, u_count)
#             fullusers.extend(
#                 api.lookup_users(user_ids=userids[i * 100:end_loc])                
#             )
#         return fullusers
#     except:
#         import traceback
#         traceback.print_exc()
#         print ('Something went wrong, quitting...')


if __name__ == '__main__':
	#pass in the username of the account you want to download
	user_ids = ['FoodandTravelEd','nytimes','premierleague','MTV','facebook','eBay','parenting']
	for i in user_ids:
		get_neighbours(i)

#user = api.get_user('myuser')
#print(dir(user))
#count the tweets api.get_user('pycon').statuses_count
#count the no of followers: 
