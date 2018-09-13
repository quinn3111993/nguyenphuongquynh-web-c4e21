from flask import Flask, render_template

app = Flask(__name__)

bmi_list = [
    'BMI < 16 : Severely underweight',
    '16 <= BMI < 18.5: Underweight',
    '18.5 <= BMI < 25: Normal',
    '25 <= BMI < 30: Overweight',
    'BMI > 30: Obese'
]

@app.route('/')
def homepage():
    return 'This is homepage'

@app.route('/bmi/<int:w>/<int:h>')
def bmi_condition(w,h):
    bmi = w/(h/100)**2
    return render_template('bmi.html',
    title='Your BMI = {0}'.format('%.2f'%bmi),
    posts=bmi_list)

print("Running app")
if __name__ == '__main__':
    app.run(debug=True)
    