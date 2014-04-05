import os, pymongo, postsDAO
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

@app.route('/')
def homePage():
	myName = posts.get_posts()
	return render_template('base.html', posts = myName)

@app.route('/faq.html')
def faqPage():
	return render_template('faq.html')

@app.route('/mostpopular.html')
def popularPage():
	return render_template('mostpopular.html')

@app.route('/submit.html')
def submitPage():
	return render_template('submit.html')

@app.route('/<postID>')
def individualPoast(postID):
	post = posts.get_post_with_ID(postID)
	return render_template('post.html',post = post)

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
