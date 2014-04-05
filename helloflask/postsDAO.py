import string

class PostsDAO(object):

	def __init__(self, database):
		self.db = database
		self.posts = database.Posts

	def get_posts(self):
		postList = []
		for post in self.posts.find():
			print post
			postList.append([post['name'], post['text'], post['url']])
		return postList

	def insert_post(self, name, text):
		urlParse = self.parseText(text)
		newPost = {"name": name, "text": text, "likes": 0, "url": urlParse}
		self.posts.insert(newPost)

	def get_post_with_url(self, url_text):
		post = self.posts.find({"url": url_text})
		return post

	def parseText(self, text):
		text = text.split()
		parse = ""
		if len(text) > 10:
			text = text[:10]
		for word in text:
			parse += word + "-"
		if parse[-1] == "-":
			parse = parse[:-1]
		return parse
		