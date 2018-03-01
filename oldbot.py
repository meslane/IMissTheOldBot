import praw
import prawcore
import time
import sys
import re
import os
import random
import math
from keys import keys 

def mainloop():
    while True:
        reddit = praw.Reddit(user_agent='I_Miss_The_Old_Bot by /u/pantumbra', 
        client_id=keys['cid'], 
        client_secret=keys['cs'], 
        username='I_Miss_The_Old_Bot', 
        password=keys['pw'])
        
        print "API Authentication Successful\n"
        
        subreddit = reddit.subreddit('all')
        comments = subreddit.stream.comments()
        
        try:
            for comment in comments:
                user = str(comment.author) #user
                body = str(comment.body.encode('ascii', 'replace')) #body
                bodylower = body.lower()
                id = comment.id #comment id 
                sub = comment.subreddit #subreddit
                
                if 'i miss the old' in bodylower and user != "I_Miss_The_Old_Bot":
                    list_of_words = body.split()
              
                    missed = list_of_words[list_of_words.index("old") + 1]
                    
                    reply = "I miss the old {0}, straight from the go {0}, chop up the soul {0}, set on his goals {0}, I hate the new {0}, the bad mood {0}, spaz in the news {0}, I miss the sweet {0}, chop up the beats {0}, I got to say at that time I'd like to meet {0}, see, I invented {0}, it wasn't any {0}s, and now I look and look around there's so many {0}s, I used to love {0}, I used to love {0}, I even had the pink polo I thought I was {0}, what if {0} made a song about {0} called 'I miss the old {0}' Man, that'd be so {0}. That's all it was {0}, we still love {0}, and I love you like {0} loves {0}.".format(missed)
                    comment.reply(reply)
                    
                    print "replied to %s" %(user)
                    
        except (prawcore.exceptions.RequestException, 
        praw.exceptions.APIException, 
        prawcore.exceptions.Forbidden):
            print "Exception encountered at %.2f, restarting to attempt reconnection\n" %(time.time())
            
            
mainloop()