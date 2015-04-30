#!/usr/bin/env python
import unicodedata
import feedparser
import ConfigParser
Config=ConfigParser.ConfigParser()
try:
  Config.read('alarm.config')
except:
  raise Exception('Sorry, Failed reading alarm.config file.')

try:
    rss = feedparser.parse('http://www.bbc.co.uk/mundo/index.xml')
    #http://www.bbc.co.uk/mundo/index.xml

#for entry in rss.entries[:4]:
#    print entry['title']
#    print entry['description']
#
#print rss.entries[0]['title']
#print rss.entries[0]['description']
#print rss.entries[1]['title']
#print rss.entries[1]['description']
#print rss.entries[2]['title']
#print rss.entries[2]['description']
#print rss.entries[3]['title']
#print rss.entries[3]['description']

    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  '+ rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  '

# print newsfeed
    f = open('newsfeed.log','w')
    newsfeed = newsfeed.encode('utf-8')
    f.write(newsfeed)
    #newsfeed = unicodedata.normalize("NFKD", newsfeed)

# Today's news from BBC
    news = 'ahora, Las ultimas noticias de BBC.  ' + newsfeed


except rss.bozo:
    news = 'Failed to reach BBC News'

if Config.get('main','debug') == str(1):
  print news
