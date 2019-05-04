#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#Author: vietjovi@gmail.com
#

import feedparser, datetime, os

#
#Functions
#

def sendToGoogleChat(urlWebhook='', msg=''):
	pass

#
#Main
#

data = []
present = datetime.datetime.utcnow()
past = present - datetime.timedelta(hours=11) #Set timedelta same time with crontab
RSS_CONF = os.path.realpath(__file__).replace("rssbot.py","rss.conf")

print present
print past

with open(RSS_CONF, "r") as f: 
	rss = f.readlines()

for i in rss:
	print i
	rss_parsed = feedparser.parse(i)
	# print rss_parsed

	for item in rss_parsed['items']:
		#Fri, 19 Apr 2019 06:00:06 +0000
		timePublished = datetime.datetime.strptime(item['published'].replace(" +0000",""), "%a, %d %b %Y %H:%M:%S")
		
		if past < timePublished:
			print item['title'] 
			print item['summary']
			print item['published']
			print item['link']
		# raw_input()
# print data