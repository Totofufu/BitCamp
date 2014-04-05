import os, pymongo, postsDAO
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/base.html')
def homePage():
	myName = posts.get_posts()
	return render_template('base.html', posts = myName[::-1])

@app.route('/faq.html')
def faqPage():
	return render_template('faq.html')

@app.route('/submit.html')
def submitPage():
	return render_template('submit.html')

@app.route('/post/<post>')
def individualPost(post):
	#thePost = posts.get_post_with_url(url_text)
	postList = posts.getText(post)
	return render_template('post.html',post = postList)

@app.route('/bestbest.html')
def bestBest():
	top10 = posts.getBestTen()
	return render_template('bestbest.html', posts = top10)

@app.route('/worstworst.html')
def worstWorst():
	worst10 = posts.getWorstTen()
	return render_template('worstworst.html', posts = worst10)

@app.route('/newpost', methods = ['GET','POST'])
def insert_newpost():
	name = request.form["name"]
	text = request.form["text"]
	posts.insert_post(name, text)
	return redirect("/")

@app.route('/upvote/<url_str>')
def incrementUpvote(url_str):
	posts.incrementUp(url_str)
	return redirect("/")

@app.route('/downvote/<url_str>')
def incrementDownVote(url_str):
	posts.incrementDown(url_str)
	return redirect("/")

@app.route('/upvotep/<url_str>')
def incrementUpvoteP(url_str):
	posts.incrementUp(url_str)
	return redirect("/post/" + url_str)

@app.route('/downvotep/<url_str>')
def incrementDownVoteP(url_str):
	posts.incrementDown(url_str)
	return redirect("/post/" + url_str)

connection_string = "mongodb://rnvarma:bitcampcmu@oceanic.mongohq.com:10011/app23759697"
#connection_string = "mongodb://localhost"

connection = pymongo.MongoClient(connection_string)
database = connection.app23759697
posts = postsDAO.PostsDAO(database)

if __name__ == '__main__':
    app.run()
