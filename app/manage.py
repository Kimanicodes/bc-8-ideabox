from flask import Flask

'''Creating an instance of the flask class'''
ideabox_app = Flask (__name__)

@ideabox_app.route('/')
def hello():
	return 'Hello IdeaBox!'

@ideabox_app.route('/Home')
def hello_home():
	return 'Hello Home'

@ideabox_app.route('/About')
def hello_about():
	return 'Hello About'
	
@ideabox_app.route('/me')
def me():
	return "First Blue print"

if __name__ == "__main__":
	ideabox_app.run(debug = True)



