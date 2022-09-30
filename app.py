from flask import Flask, render_template, request 
import joblib
from  predict.pred import f_prediction 

app = Flask(__name__)

# code logib

@app.route('/')
def base():
    return render_template('main.html')

@app.route('/home')
def galery():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return 'Contact information'

@app.route('/predict', methods=['POST'])
def predict():

    # load the model
    # model = joblib.load('diabetic_80.pkl')

    preg = request.form.get('preg')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')

    print(preg)
    print(age)

    # call prediction function 
    data = f_prediction(preg, plas, pres, skin, test, mass, pedi, age)

    return render_template('predict.html', data = data)

# app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)



