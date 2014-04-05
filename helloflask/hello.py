import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homePage():
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

if __name__ == '__main__':
    app.run()
