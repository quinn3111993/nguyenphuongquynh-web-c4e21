from flask import Flask, render_template, request
import mlab
from user import User
from string import punctuation

app = Flask(__name__)
mlab.connect()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        #1. Get form & extract data
        form = request.form
        a = form['name']
        b = form['email']
        c = form['user_name']
        d = form['password']
        set_d = set(d)
        set_special = set(punctuation)
        if '@' not in b or '.' not in b:
            return 'Invalid Email adress'
        elif len(d) < 6:
            return 'Password must be longer than 6 chars'
        elif list(set_d & set_special) == []:
            return 'Password must contain special chars'

        print(a, b, c, d)

        #2. Add new post
        new_user = User(name=a, email=b, user_name=c, password=d)
        new_user.save()

        return 'OK'

if __name__ == '__main__':
    app.run(debug=True)