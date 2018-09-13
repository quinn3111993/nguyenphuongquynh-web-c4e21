#1. Create a flask app
from flask import Flask, render_template

app = Flask(__name__)

ps = [
        'Trong đầm gì đẹp bằng sen',
        'Lá xanh bông trắng lại chen nhị vàng',
        'Nhị vàng bông trắng lá xanh',
        'Gần bùn mà chẳng hôi tanh mùi bùn'
        ]

ps_new = [ele[:20] for ele in ps]

#2. Create router
@app.route('/')
def homepage():
    return render_template('homepage.html', 
    title='My title', 
    posts=ps)

@app.route('/quinn')
def quinn():
    return 'Hello Quinn'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello ' + name

@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return str(x+y)

@app.route('/h1tag')
def h1tag():
    return '<h1>Heading 1 - Biggg</h1><p>Hom nay toi buon</p>'

@app.route('/post/<int:x>')
def post(x):
    post = ps[x-1]
    if x > len(ps):
        return 'Not found'
    else:
        return render_template('postdetail.html', 
        title='My title', 
        post=post)

@app.route('/posts')
def posts():
    return render_template('homepage.html', 
    title='My title', 
    posts=ps_new)

#3. Run app
print("Running app")
if __name__ == '__main__':
    app.run(debug=True) # listening