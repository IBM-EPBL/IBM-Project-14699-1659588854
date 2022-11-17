import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('prediction.html')
# prediction function

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,11)
    model = pickle.load(open("smart_lender.pkl", "rb"))
    prediction = model.predict(to_predict)
    return prediction[0]

@app.route('/prediction', methods = ['POST'])
def prediction():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        prediction = ValuePredictor(to_predict_list)
        if int(prediction)== 1:
            pred ='Loan_Approved'
        else:
            pred ='Loan_Not_Approved'
                
        return render_template('result.html', prediction_text = "Loan Status - {}".format(pred))
    

if __name__ == "__main__":
    app.run(debug=True)