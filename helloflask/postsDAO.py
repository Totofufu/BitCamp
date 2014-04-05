import string

class PostsDAO(object):

	def __init__(self, database):
		self.db = database
		self.posts = database.Posts

	def get_posts(self):
		postList = []
		for post in self.posts.find():
			print post
			postList.append((post['name'], post['text']))
		return postList

	def insert_post(self, name, text):
		newPost = {'name': name, "text": text}
		self.posts.insert(newPost)
		