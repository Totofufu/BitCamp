import string

class PostsDAO(object):

	def __init__(self, database):
		self.db = database
		self.posts = database.Posts

	def get_posts(self):
		postList = []
		for post in self.posts.find():
			print post
			postList.append([post['name'], post['text'], post['_id']])
		return postList

	def insert_post(self, name, text):
		newPost = {"name": name, "text": text, "likes": 0}
		self.posts.insert(newPost)

	def get_post_with_ID(self, postID):
		post = self.posts.find({_id: postID})
		return post
		