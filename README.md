Intro
=====
A readability metric identifier for news articles. Article text is retrieved via respective news outlets' api. Ten articles on the desired subject are retrieved to be measured and their aggregate score for each measure is printed out.  

Howto
=====
Be sure to first sign up to the appropriate news outlet to retrieve your api key.
	$cd readability
	$python newsreader.py
From here you'll be prompted on the cmd line on your desired news outlet and subsequently on your desired topic. The program will then retrieve 10 of the latest articles in that subject and print out the readability scores. 

APIs
=====
Currently Used API:
------------------
www.npr.org/api/index

Failed usage of these APIs:
--------------------------n
developer.nytimes.com
apiportal.washingtonpost.com
developer.usatoday.com

Most of the apis are pending due to the lack of access to the full article. The above api only allows at most a snippet and/or a url. The usage of a web scraper is not viable for news articles as these news outlets typically have limits to article views for non-subscribed users. 

Currently Available Topics
==========================
*In no particular order*
-Science
-Economy
-US 
-World
-Politics
-Education
-Technology
-Business

NPR topic ids can be found here: http://www.npr.org/api/mappingCodes.php . Just add the topic id to the News class dictionary NPR_TOPIC_IDS. 

Acknowledgements
-https://github.com/mmautner/readability 
-https://github.com/nltk/nltk_contrib/tree/master/nltk_contrib/readability
	
The links to each measures' descriptions as posted in mmautner's readme are as follows:
-http://en.wikipedia.org/wiki/Automated_Readability_Index
-http://en.wikipedia.org/wiki/SMOG
-http://en.wikipedia.org/wiki/Flesch%E2%80
93Kincaid_Grade_Level#Flesch.E2.80.93Kincaid_Grade_Level
-http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_test#Flesch_Reading_Ease
-http://en.wikipedia.org/wiki/Coleman-Liau_Index
-http://en.wikipedia.org/wiki/Gunning-Fog_Index
