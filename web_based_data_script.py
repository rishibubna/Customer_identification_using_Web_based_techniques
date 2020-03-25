#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv
import json
#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True, compression=True)

def get_neighbours(screenname):
	data_dict = {}
	data_dict[screenname] = {}
	followee = []
	followers = []
	# for pg in tweepy.Cursor(api.followers, screen_name=screenname).items(100):
	# 	print(pg)
	# 	print("---------------------------")
	for user in tweepy.Cursor(api.followers, screen_name=screenname).items(50):
	#(int(user.followers_count)+int(user.friends_count) > 500)
		if  (user.protected == False) and (int(user.statuses_count) >= 0):
			print("in followers loop")
			screen_name_user, user_tweets = get_all_tweets(user.screen_name)

			data_dict[screenname][user.screen_name] = {}
			data_dict[screenname][user.screen_name]['tweets']=user_tweets
			data_dict[screenname][user.screen_name]['location']=user.location
			count = 0
			count_friends = 0
			print("------------------------------")
			for sc_user in tweepy.Cursor(api.followers, screen_name=screen_name_user).items(10):
				if (sc_user.protected == False) and (int(sc_user.statuses_count) >= 200) and (int(user.followers_count)<=1000):
					follower_user, follower_user_tweets = get_all_tweets(sc_user.screen_name)
					data_dict[screenname][screen_name_user][follower_user] = {}
					data_dict[screenname][screen_name_user][follower_user]['tweets']=follower_user_tweets
					data_dict[screenname][screen_name_user][follower_user]['location']=sc_user.location
					count += 1
					print(count)
			with open('web_based_data_10followers.json', 'w') as outfile:
				json.dump(data_dict, outfile)
			for fr_user in tweepy.Cursor(api.friends, screen_name=screen_name_user).items(10):
				if (fr_user.protected == False) and (int(fr_user.statuses_count) >= 200) and (int(fr_user.followers_count)<=1000):
					followee_user, followee_user_tweets = get_all_tweets(fr_user.screen_name)
					data_dict[screenname][screen_name_user][followee_user] = {}
					data_dict[screenname][screen_name_user][followee_user]['tweets']=followee_user_tweets
					data_dict[screenname][screen_name_user][followee_user]['location']=fr_user.location
					count_friends += 1
					print(count_friends)
	print(data_dict)

	with open('web_based_data_followers.json', 'w') as outfile:
		json.dump(data_dict, outfile)

def get_all_tweets(screen_name):
	#initialize a list to hold all the tweepy Tweets#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=1)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	#save the id of the oldest tweet less one
	if len(alltweets)>0:
		oldest = alltweets[-1].id - 1
	#keep grabbing tweets until there are no tweets left to grab
		while len(alltweets) < 10 and len(new_tweets) > 0:
			# print("getting tweets before %s" % (oldest))
			#all subsiquent requests use the max_id param to prevent duplicates
			new_tweets = api.user_timeline(screen_name = screen_name,count=1,max_id=oldest)
			#save most recent tweets
			alltweets.extend(new_tweets)
			#update the id of the oldest tweet less one
			oldest = alltweets[-1].id - 1
			
			# print("...%s tweets downloaded so far" % (len(alltweets)))

	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.text] for tweet in alltweets]
	print(screen_name)
	print("...%s tweets downloaded" % (len(alltweets)))

	print('...............................')
	return screen_name, outtweets


if __name__ == '__main__':
	#pass in the username of the account you want to download
	# user_ids = ['FoodandTravelEd','nytimes','premierleague','MTV','facebook','eBay','parenting']
	# for i in user_ids:
	get_neighbours('tesla')

#user = api.get_user('myuser')
#print(dir(user))
#count the tweets api.get_user('pycon').statuses_count
#count the no of followers: 
