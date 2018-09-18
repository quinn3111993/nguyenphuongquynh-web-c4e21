from flask import Flask, render_template, request
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

p = {
    'title': 'C4E21',
    'content': 'Module web',
    'author': 'Quinn',
    'date': '2018/09/02',
}

ps = [
  {
    'title': 'C4E21',
    'content': 'Module web',
    'author': 'Quinn',
    'date': '2018/09/02',
  },
  {
    'title': 'techkids',
    'content': 'No content here',
    'author': 'Quynh',
    'date': '2018/09/04',
  },
  {
    'title': 'python class',
    'content': 'Fundamental things',
    'author': 'Huy',
    'date': '2018/09/15',
  }
]

@app.route('/post')
def post():
    return render_template('dict.html', post=p)

@app.route('/posts')
def posts():
    return render_template('dicts.html', posts=ps)

@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('new_post.html')
    elif request.method == 'POST':
        #1. Get form & extract data
        form = request.form
        t = form['title']
        a = form['author']
        c = form['content']
        print(t, a, c)

        #2. Add new post
        new_post = Post(title=t, author=a, content=c)
        new_post.save()

        return 'OK'

if __name__ == '__main__':
    app.run(debug=True)