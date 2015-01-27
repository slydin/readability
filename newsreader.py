import os
import sys
from urllib2 import urlopen
from json import load
from readability import Readability

class News:
	
	"""NYT Developer API, WP Developer API and USA Developer API do not 
	allow for full body text retrieval thus it will not be used at the moment"""
	NPR_KEY = "API_KEY" #www.npr.org/api/index
	NYT_KEY = "API_KEY" #developr.nytimes.com
	WP_KEY = "API_KEY" #apiportal.washingtonpost.com
	USA_KEY = "API_KEY" #developer.usatoday.com
	
	NPR_TOPIC_IDS = {"science": "1007","economy":"1039","us":"1003",
"world":"1004","politics":"1014","education":"1013",
"technology":"1019","business":"1006"}
	NYT_TOPIC_IDS = {}
	outlets = ["NPR"]
	
	def __init__(self,name):
		self.news = ""		
		if name.upper() in News.outlets:		
			self.news = name.upper()
		else:
			print("Cannot access that news outlet")
			sys.exit(1)

		self.uri = ""
		if self.news == "NPR":
			self.uri = "http://api.npr.org/query?apiKey=" + News.NPR_KEY + "&format=json&requiredAssests=text&numResults=10"
		

	def get_topic_ids(self, topic):
		if self.news == "NPR":
			if topic.lower() in News.NPR_TOPIC_IDS.keys():
				self.uri += "&id=" + News.NPR_TOPIC_IDS[topic.lower()]
				return
			else
				print("Topic not available")
				sys.exit(1)

		return None # maybe an empty string is better

	def get_articles(self):
		articles = ""
		if self.news == "NPR":
			response = urlopen(self.uri)
			json_obj = load(response)
			for story in json_obj['list']['story']:
				print("Title: " + story['title']['$text'] + "\n")
				for paragraph in story['text']['paragraph']:
					if '$text' in paragraph.keys():
						articles += paragraph['$text'] + "\n"
		return articles
								
def main():
	
	news_source = raw_input("Please input desired news source: (e.g NPR)")
	news_topic = raw_input("Please input desired topic: (e.g Science)")
	news = News(news_source)
	news.get_topic_ids(news_topic)
	print(news.uri)
	articles = news.get_articles()
	articles = articles.encode('ascii','xmlcharrefreplace') # need to look into this more

	#Generate scorer
	h = Readability(articles)
	#scores
	print("ARI: {:f}".format(h.ARI()))
	print("Flesch_Reading_Ease: {:f}".format(h.FleschReadingEase()))
	print("Flesch_Kincaid_Grade_Level: {:f}".format(h.FleschKincaidGradeLevel()))
	print("Gunning_Fog_Index: {:f}".format(h.GunningFogIndex()))
	print("SMOG_Index: {:f}".format(h.SMOGIndex()))
	print("Coleman_Liau_Index: {:f}".format(h.ColemanLiauIndex()))
	print("LIX: {:f}".format(h.LIX()))
	print("RIX: {:f}".format(h.RIX()))
	
if __name__ == '__main__':
	main()
