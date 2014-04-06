import os, pymongo, postsDAO
from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

@app.route('/')
@app.route('/<pageNum>')
@app.route('/base.html')
def homePage(pageNum = 1):
    pageNum = int(pageNum)
    if (pageNum == 1): has_back = False
    else: has_back = True
    myName = posts.get_posts()
    lenOfMyName = len(myName)
    myName = myName[::-1]
    postNum = (pageNum-1)*10 
    if (10*pageNum <= lenOfMyName):
        myName = myName[postNum:postNum+10]
        has_next = True
    else:
        myName = myName[postNum:]
        has_next = False
    #define all 4 scenarios
    #no back or next
    if not (has_next or has_back): no_move = True
    else: no_move = False
    #on first page, so no back, but 10+ posts
    if (has_next and not has_back): next = True
    else: next = False
    #on last page
    if (not has_next and has_back): back = True
    else: back = False
    #has both back and next buttons
    if (has_next and has_back): both = True
    else: both = False
    return render_template('base.html', posts = myName, pageNBack = pageNum-1, 
        pageNNext = pageNum+1, pageN = pageNum, noMove = no_move, goNext = next, goBack = back, 
        goBoth = both)

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

@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/newpost', methods = ['GET','POST'])
def insert_newpost():
    name = request.form["name"]
    text = request.form["text"]
    posts.insert_post(name, text)
    return redirect("/")

@app.route('/makesearch', methods = ["GET", "POST"])
def make_search():
    print 1
    query = request.form["query"]
    print 2
    postList = posts.makeSearch(query)
    return render_template('searchResults.html', posts = postList)

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
    app.debug = True
    app.run()
