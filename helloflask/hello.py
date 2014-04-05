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

@app.route('/mostpopular.html')
def popularPage():
	return render_template('mostpopular.html')

@app.route('/submit.html')
def submitPage():
	return render_template('submit.html')

@app.route('/bestbest.html')
def bestBest():
	return render_template('bestbest.html')

@app.route('/worstworst.html')
def worstWorst():
	return render_template('worstworst.html')

@app.route('/post/<url_text>')
def individualPost(url_text):
	thePost = posts.get_post_with_url(url_text)
	return render_template('post.html',post = thePost)

@app.route('/newpost', methods = ['GET','POST'])
def insert_newpost():
	name = request.form["name"]
	text = request.form["text"]
	posts.insert_post(name, text)
	return render_template('base.html', posts = posts.get_posts())

connection_string = "mongodb://rnvarma:bitcampcmu@oceanic.mongohq.com:10011/app23759697"
#connection_string = "mongodb://localhost"

connection = pymongo.MongoClient(connection_string)
database = connection.app23759697
posts = postsDAO.PostsDAO(database)

if __name__ == '__main__':
    app.run()
