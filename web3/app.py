from flask import Flask, render_template, request, redirect, url_for
import mlab
from post import Post

app = Flask(__name__)
mlab.connect()

@app.route('/')
def home():
    return redirect('/posts')

@app.route('/post/<post_id>')
def post(post_id):
    all_posts = Post.objects()
    post = all_posts.with_id(post_id)
    if post is None:
        print('Not found')
    else:
        return render_template('post.html', post=post)

@app.route('/delete/<post_id>')
def delete(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect(url_for('posts'))

@app.route('/update/<post_id>', methods=['GET', 'POST'])
def update(post_id):
    post = Post.objects().with_id(post_id)
    if request.method == 'GET':
        return render_template('update_post.html', old_post=post)
    elif request.method == 'POST':
        #1. Get form & extract data
        form = request.form
        t = form['title']
        a = form['author']
        c = form['content']
        print(t, a, c)  
        #2. Update new post
        post.update(set__title=t, set__author=a, set__content=c) #inc_likes #push__
        #post.reload()
    return redirect('/post/'+post_id)

@app.route('/posts')
def posts():
    all_posts = Post.objects()
    return render_template('posts.html', posts=all_posts)


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

        return redirect(url_for('posts'))

if __name__ == '__main__':
    app.run(debug=True)