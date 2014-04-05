import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def homePage():
  return render_template('base.html')

if __name__ == '__main__':
    app.run()
