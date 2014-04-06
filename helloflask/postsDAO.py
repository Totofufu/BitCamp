import string
from datetime import datetime

class PostsDAO(object):

	def __init__(self, database):
		self.db = database
		self.posts = database.Posts

	def get_posts(self):
		postList = []
		for post in self.posts.find():
			if post['likes'] + post['dislikes'] > 0:
				color = self.makePixel(int(post['likes']), int(post['dislikes']))
			else: color = "black"
			postList.append([post['name'], post['text'], post['url'], post['likes'], post['dislikes'], color,
							post['tf']])
		return postList

	def insert_post(self, name, text):
		datetime.now()
		urlParse = self.parseText(text)
		dateStr = str(datetime.now())
		date = self.parseDate(dateStr)
		print date
		newPost = {
			"name": name, "text": text, "likes": 0, "dislikes": 0, "url": urlParse, "tf": date }
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

	def getBestTen(self):
		top10List = []
		for post in self.posts.find():
			if post['likes'] + post['dislikes'] > 0:
				color = self.makePixel(int(post['likes']), int(post['dislikes']))
			else: color = "black"
			top10List.append([post['name'], post['text'], post['url'], post['likes'], post['dislikes'], color,
							post['tf']])
		top10List.sort(likesCmp)
		if len(top10List) >= 10:
			return top10List[:10]
		else: return top10List

	def getWorstTen(self):
		top10List = []
		for post in self.posts.find():
			if post['likes'] + post['dislikes'] > 0:
				color = self.makePixel(int(post['likes']), int(post['dislikes']))
			else: color = "black"
			top10List.append([post['name'], post['text'], post['url'], post['likes'], post['dislikes'], color,
							post['tf']])
		top10List.sort(dislikesCmp)
		if len(top10List) >= 10:
			return top10List[:10]
		else: return top10List

	def getText(self,url):
		for post in self.posts.find():
			if post["url"] == url:
				if post['likes'] + post['dislikes'] > 0:
					color = self.makePixel(int(post['likes']), int(post['dislikes']))
				else: color = "black"
				return [post["text"],post["name"],post["url"], post["likes"], post["dislikes"], color,
						post['tf']]

	def incrementUp(self, url_str):
		self.posts.update({"url":url_str},{"$inc":{"likes":1}})

	def incrementDown(self, url_str):
		self.posts.update({"url":url_str},{"$inc":{"dislikes":1}})

	def makePixel(self, likes, dislikes):
		redD = 255*(float(likes)/(dislikes+likes))
		greenD = 255 - redD
		color = "#" + self.decToHex(greenD) + self.decToHex(redD) + "00"
		return color

	def decToHex(self, dec):
		decToHex = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
		firstDig = int(dec) / 16
		secondDig = int(dec) % 16
		if firstDig > 9:
			firstDig = decToHex[firstDig]
		if secondDig > 9:
			secondDig = decToHex[secondDig]
		return str(firstDig) + str(secondDig)

	def parseDate(self, dateStr):
		months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
		date, time = dateStr.split()
		year = date[:4]
		month = months[int(date[5:7])]
		day = date[8:]
		hour, minute, seconds = time.split(":")
		if int(hour) >= 12:
			amorpm = "PM"
		else: amorpm = "AM"
		if int(hour) != 12:
			hour = str(int(hour) % 12)
		if int(hour) == 0: hour = "12"
		timeStamp = month + " " + day + ", " + year + ". " + hour + ":" + minute + " " + amorpm + "."
		return timeStamp



def likesCmp(a1, a2):
	return a2[3] - a1[3]

def dislikesCmp(a1, a2):
	return a2[4] - a1[4]


		