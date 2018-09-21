from flask import Flask, render_template, redirect, request, url_for
import mlab
from review import Review

app = Flask(__name__)
mlab.connect()

@app.route('/new-review', methods=['GET', 'POST'])
def new_review():
    if request.method == 'GET':
        return render_template('new_review.html')
    elif request.method == 'POST':
        form = request.form
        au = form['author']
        s = form['song']
        ar = form['artist']
        c = form['content']
        print(au, s, ar, c)

        new_review = Review(author=au, song=s, artist=ar, content=c)
        new_review.save()

        return redirect(url_for('reviews'))

@app.route('/reviews')
def reviews():
    all_reviews = Review.objects()
    return render_template('reviews.html', reviews=all_reviews)

@app.route('/review/<id>')
def review(id):
    review = Review.objects().with_id(id)
    if review is None:
        return 'Not found'
    else:
        return render_template('review.html', review=review)

@app.route('/delete/<id>')
def delete(id):
    review = Review.objects().with_id(id)
    review.delete()
    return redirect(url_for('reviews'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    review = Review.objects().with_id(id)
    if request.method == 'GET':
        return render_template('update_review.html', review=review)
    elif request.method == 'POST':
        form = request.form
        au = form['author']
        s = form['song']
        ar = form['artist']
        c = form['content']
        print(au, s, ar, c)

        review.update(set__author=au, set__song=s, set__artist=ar, set__content=c)

    return redirect('/review/'+id)
    

    




if __name__ == '__main__':
    app.run(debug=True)

