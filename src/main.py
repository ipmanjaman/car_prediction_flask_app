from flask import Flask, jsonify, render_template, request
import psycopg2
from customers import Customers
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


app = Flask(__name__,template_folder='templates')
conn = psycopg2.connect(database='car_purchase', user='pallisingh')
cursor = conn.cursor()
model = pickle.load(open('model.pickle', 'rb'))



@app.route('/')
def welcome():
    return render_template('index.html')

user = request.args.get('user')
@app.route("/predict", methods = ['GET', 'POST'])
def generate_predictions():
    if request.method == 'POST':
        age = request.form['age']
        annual_salary = request.form['annual_salary']
        credit_card_debit = request.form['credit_card_debit']
        net_worth =  request.form['net_worth']
        all_input_data = [ [age, annual_salary, credit_card_debit, net_worth] ]
        prediction = model.predict(all_input_data)
        result = prediction[0]
        return render_template("index.html", message=f"The customer can easily buy car around $ {result}")


@app.route('/customers')
def show_data():
    cursor.execute('select * from car_purchasing')
    records = cursor.fetchall()
    customers_records = [Customers(cust).__dict__ for cust in records]
    return jsonify(customers_records)

app.run(debug=True)