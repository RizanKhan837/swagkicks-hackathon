from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
#from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from resume import run
import os
import mysql.connector

load_dotenv()
app = Flask(__name__)
CORS(app, origins='http://localhost:5173')
result = ""
@app.route("/flask/hello")
def hello():
    return "My Data from Flask API"

@app.route("/") #comment this on deployment
def helloReact():
    return send_from_directory('frontend/dist','index.html')


@app.route('/orders')
def get_orders():
    # Establish a new connection
    connection = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        database="sql6634457",
        user="sql6634457",
        password="kIkvSDci1i",
        port=3306
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    results = cursor.fetchall()

    orders = []
    for result in results:
        order = {
            'ID': result[0],
            'title': result[1],
            'price': result[2],
            'discount': result[3]
        }
        orders.append(order)
    cursor.close()
    connection.close()

    return jsonify(orders)



@app.route('/translate-query', methods=['POST'])
@cross_origin()
def translate_query():
    prompt = request.json['query']
    run_result = run(prompt)
    return jsonify({
        'pdf': run_result
    })

if __name__ == '__main__':
   app.run(debug=True)