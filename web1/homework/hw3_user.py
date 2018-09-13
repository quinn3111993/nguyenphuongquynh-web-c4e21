from flask import Flask, render_template

app = Flask(__name__)

Users = {
'huy' : {
			'name' : 'Nguyen Quang Huy',
			'age' : 29
       },
'tuananh' : {
			'name' : 'Huynh Tuan Anh',
			'age' : 22
       }
}

for user in Users:
    Users[user] = [key+': '+str(Users[user][key]) for key in Users[user]]

@app.route('/')
def homepage():
    return 'This is homepage'

@app.route('/user/<username>')
def user_profile(username):
    if username in Users:
        return render_template('user.html',
        title='User profile',
        posts=Users[username])
    else:
        return 'User not found'

print("Running app")
if __name__ == '__main__':
    app.run(debug=True)

