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
    return '<h1>Your BMI = {0}</h1><p>BMI < 16 : Severely underweight</p><p>16 <= BMI < 18.5: Underweight</p><p>18.5 <= BMI < 25: Normal</p><p>25 <= BMI < 30: Overweight</p><p>BMI > 30: Obese</p>'.format('%.2f'%bmi)
    

print("Running app")
if __name__ == '__main__':
    app.run(debug=True)
    