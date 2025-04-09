from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pickle
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # needed for session handling

# Load your model
model_path = os.path.join('models', 'model.pkl')
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def page1():
    return render_template('page1.html')

@app.route('/page2', methods=['POST'])
def page2():
    session['fixed_acidity'] = request.form['fixed_acidity']
    session['volatile_acidity'] = request.form['volatile_acidity']
    session['citric_acid'] = request.form['citric_acid']
    session['residual_sugar'] = request.form['residual_sugar']
    return render_template('page2.html')

@app.route('/page3', methods=['POST'])
def page3():
    session['chlorides'] = request.form['chlorides']
    session['free_sulfur_dioxide'] = request.form['free_sulfur_dioxide']
    session['total_sulfur_dioxide'] = request.form['total_sulfur_dioxide']
    session['density'] = request.form['density']
    return render_template('page3.html')

@app.route('/predict', methods=['POST'])
def predict():
    session['pH'] = request.form['pH']
    session['sulphates'] = request.form['sulphates']
    session['alcohol'] = request.form['alcohol']

    features = [float(session[key]) for key in [
        'fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
        'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
        'pH', 'sulphates', 'alcohol'
    ]]
    
    prediction = model.predict([features])[0]
    return render_template('result.html', prediction=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
