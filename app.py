import numpy as np
import pickle
from flask import Flask,render_template,request

#Create a flask object
app=Flask(__name__)
#Loading the pickle files(model)
regmodel=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('sb.html')       

@app.route('/predict',methods=['POST'])
def predict():
    #print(request.form)
    open = float(request.form['Open Values'])
    high = float(request.form['High Values'])
    low = float(request.form['Low Values'])
    volume = float(request.form['Volume Values'])
    final_input = np.array([[open, high, low, volume]])
    output=regmodel.predict(final_input)[0]
    print('--------------------------',output)
    return render_template('sb.html', prediction_text="The Stock Price is {}".format(output))

if __name__ == '__main__':
    app.run()
