#Serve a webpage on http://localhost:65010/ that creates an "authorization" link out to reddit.com:
CLIENT_ID = "p-jcoLKBynTLew"
CLIENT_SECRET = "gko_LXELoV07ZBNUXrvWZfzE3aI"
REDIRECT_URI = "http://localhost:65010/reddit_callback"


from flask import Flask 
app = Flask(__name__)
@app.route('/')

def homepage():
  text = '<a href="%'