import string

class PostsDAO(object):

	def __init__(self, database):
		self.db = database
		self.posts = database.Posts

	def get_posts(self):
		postList = []
		for post in self.posts.find():
			likes, dislikes = int(post['likes']), int(post['dislikes'])
			#redD = 255*(float(likes)/(dislikes+likes))
			#greenD = 255 - redD
			#color = "#" + decToHex(redD) + decToHex(greenD) + "00"
			postList.append([post['name'], post['text'], post['url'], likes, dislikes])
		return postList

	def insert_post(self, name, text):
		urlParse = self.parseText(text)
		newPost = {"name": name, "text": text, "likes": 0, "dislikes": 0, "url": urlParse}
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

	def getText(self,url):
		for post in self.posts.find():
			if post["url"] == url:
				return [post["text"],post["name"],post["url"], post["likes"], post["dislikes"]]

	def incrementUp(self, url_str):
		self.posts.update({"url":url_str},{"$inc":{"likes":1}})

	def incrementDown(self, url_str):
		self.posts.update({"url":url_str},{"$inc":{"dislikes":1}})

	def decToHex(self, dec):
		decToHex = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
		firstDig = int(dec) / 16
		secondDig = int(dec) % 16
		if firstDig > 9:
			firstDig = decToHex[firstDig]
		if secondDig > 9:
			secondDig = decToHex[secondDig]
		return str(firstDig) + str(secondDig)






		