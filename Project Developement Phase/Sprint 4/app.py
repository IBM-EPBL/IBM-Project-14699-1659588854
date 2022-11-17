from flask import render_template,Flask,request,jsonify
import numpy as np
import pickle 
from sklearn.preprocessing import scale
app= Flask(__name__, template_folder='templates')

model = pickle.load(open("smart_lender.pkl",'rb'))



@app.route('/')
def home():
    return render_template('home.html')
@app.route('/home.html')
def home1():
    return render_template('home.html')
@app.route('/prediction.html')
def formpg():
    return render_template('prediction.html')
@app.route('/prediction')
def formp():
    return render_template('result.html')
@app.route('/rating.html')
def rat():
    return render_template('rating.html')
@app.route('/prediction.html',methods = ['POST','GET'])
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,11)
    model = pickle.load(open("smart_lender.pkl", "rb"))
    prediction = model.predict(to_predict)
    return prediction

@app.route('/prediction', methods = ['POST','GET'])
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