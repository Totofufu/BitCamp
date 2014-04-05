import os, pymongo, postsDAO
from flask import Flask, render_template, redirect, request


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
	name = request.forms["name"]
	text = request.forms["text"]
	posts.insert_post(name, text)
	redirect('/')

connection_string = "mongodb://rnvarma:bitcampcmu@oceanic.mongohq.com:10011/app23759697"

connection = pymongo.MongoClient(connection_string)
database = connection.app23759697
posts = postsDAO.PostsDAO(database)

if __name__ == '__main__':
    app.run()
