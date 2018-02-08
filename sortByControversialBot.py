#!/usr/bin/python
import praw
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

def store_controversial_comments(current_post, controversial_comments):
	url = "https://www.reddit.com/" + current_post + "/?sort=controversial"
	print url
	# TODO get the controversial posts from this link and store it
	return controversial_comments

def scan_subreddits():
	for comment in subreddit.stream.comments():
		# print(comment.body)
		if re.search("sort by controversial", comment.body, re.IGNORECASE):
			controversial_comments = []
			controversial_comments = store_controversial_comments(str(comment.submission), controversial_comments)
			bot_reply = "Here's a sneak peek of the most controversial comments: " + str(controversial_comments)
			bot_reply = controversial_comments
			# comment.reply(bot_reply)
			print(bot_reply)

if __name__ == "__main__":
	try:
		scan_subreddits()
	except praw.exceptions.APIException as e_API:
		pass