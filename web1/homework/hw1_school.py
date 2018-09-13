from flask import Flask, render_template, redirect

app = Flask(__name__)

dic = {
    'name': 'Quinn',
    'age': 25,
    'school': 'FTU',
    'job': 'a kid in tech',
}

my_info = [key+': '+str(dic[key]) for key in dic]

print(my_info)

@app.route('/')
def homepage():
    return 'This is homepage'

@app.route('/about-me')
def about_me():
    return render_template('about_me.html',
    title='Hi! Let me introduce about myself',
    infos=my_info)

@app.route('/school')
def techkid():
    return redirect('http://techkids.vn', code=302)

print("Running app")
if __name__ == '__main__':
    app.run(debug=True)