import os, pymongo, postsDAO
from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def homePage():
	posts_list = posts.get_posts()
	return render_template('base.html')

@app.route('/faq.html')
def faqPage():
	return render_template('faq.html')

@app.route('/mostpopular.html')
def popularPage():
	return render_template('mostpopular.html')

@app.route('/submit.html')
def submitPage():
	return render_template('submit.html')

@app.route('/newpost', methods = ['POST'])
def insert_newpost():
	name = bottle.request.forms.get("name")
	text = bottle.request.forms.get("text")
	posts.insert_post(name, text)
	app.redirect('/')

connection_string = "mongodb://rnvarma:bitcampcmu@oceanic.mongohq.com:10011/app23759697"

connection = pymongo.MongoClient(connection_string)
database = connection.Posts
posts = decisionPostsDAO.decisionPostsDAO(database)

if __name__ == '__main__':
    app.run()
