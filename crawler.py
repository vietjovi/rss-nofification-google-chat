#vietjovi@gmail.com
import feedparser, datetime

def sendToGoogleChat(urlWebhook='', msg=''):
	pass

data = []
dateNow = dt = datetime.datetime.utcnow()

with open("rss.conf", "r") as f: 
	rss = f.readlines()

for i in rss:
	print i
	rss_parsed = feedparser.parse(i)
	# print rss_parsed

	titles = [art['title'] for art in rss_parsed['items']]

	#Creat dict
	d = {
	    'title':titles,
	    'datetime':dateNow
	}
	data.append(d)
print data