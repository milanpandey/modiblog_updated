from django.core.management.base import NoArgsCommand
from blog_entry.models import Entry
import feedparser


def is_new(feed):
	try:
		post = Entry.objects.get(guid = feed.id)
	except Entry.DoesNotExist:
		return True 
	return False 

class Command(NoArgsCommand):
    help = "Gets the Feed from Google News"
    def handle_noargs(self, **options):
    	print "Getting the Feed From Google News"
    	feed = feedparser.parse("https://news.google.co.in/news/feeds?um=1&ned=us&hl=en&q=Narendra+Modi&output=rss")
    	print "Finished Getting the Feed from Google News"
    	for post in feed.entries :
    		if(is_new(post)):
    			print "Save the feed since it is new"
    			p = Entry(guid = post.id , title=post.title , body = post.description)
    			p.save() ; 
    		else:
    			print "Ignoring the feed since it has already been seen"
    	



