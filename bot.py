import praw
import config
import re
from gui import display
# Setting up Reddit Bot using PRAW and things we set in config
def bot_login():
    r = praw.Reddit(
        username = config.username,
        password = config.password,
        client_id = config.client_id,
        client_secret = config.client_secret,
        user_agent = "One Piece latest spoiler bot"
    )
    return r 


# Chapter Dictionary set up as a global variable incase we need to access it anywhere
chapter_dict= {} 




def run_bot(r):
    #Go to the subreddit /r/OnePiece
    subreddit = r.subreddit("OnePiece")

    #Go to the Spoiler Thread, since we are checking for the LATEST chapter spoiler there's a limit of at least 5.
    submissions = subreddit.search('flair: "Spoiler thread"', limit=3)

    #Setting up a list so we can format and get each individual page rather than a block of text
    pages = []

    #For loop to go through each submission(Each reddit post), pull the text/title, format it, and store it in the chapter_dict
    for s in submissions:
        #Gets each new line and splits it
        lines = s.selftext.split("\n")

        #For loop to go through each 'Page' and format it to be legible
        for line in lines:
            pages.append(line) #First is the page number, second is the line of text associated with the page

        #Updates dictionary with the new Chapter and it's corresponding pages EX: {1071: [these, are, the, pages]}            
        chapter_dict.update({int(re.search(r"\b\d+\b", s.title).group()): pages})

    latest_chapter(chapter_dict)
    display(chapter_dict)

def save_chapter(chapter):
    with open('chapter.txt', 'w') as f:
        f.write(str(chapter))

def latest_chapter(chapter_dict):
    try:
        with open('chapter.txt', 'r') as f:
            latest_chap = int(f.read())
    except:
        print("Thanks for using OneSpoiler, setting up first time things...")
        latest_chap = 0

    updated = False

    for chap_num in chapter_dict.keys():
        if chap_num > latest_chap:
            latest_chap = chap_num
            updated = True

    if updated:
        print("Found a new chapter!")
        print("Latest Chapter is {}".format(latest_chap))         
        save_chapter(latest_chap)
    else:
        print("No new chapter available, wait a couple of days and try again!")

run_bot(bot_login())


print("Done!")