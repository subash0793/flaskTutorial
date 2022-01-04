from flask import Flask, render_template
from markupsafe import escape
app = Flask(__name__)

 #list of dictionaries
posts= [
           {'author': "subash",
            'title':"bg 1",
            'date':'apr 1'
            },
            {'author': "Gautam",
            'title':"bg 2",
            'date':'apr 2'
            }


]

@app.route("/")
def home_page():
    return render_template('home.html', posts=posts)
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/<name>")
def name(name):
    return "Hello " + name

def newName(name):
    return name

@app.route("/about")
def about_page():
   return render_template('about.html',title="About Page")

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

def newtrythin():
    return "just try"

def secondtry():
    return "this is second try"
if __name__== '__main__':
    app.run(debug=True)