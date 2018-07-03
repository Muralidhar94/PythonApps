import os
import psycopg2
from flask import Flask
from flask import Response
from flask.json import jsonify
import json
import http

app=Flask(__name__)
@app.route('/getEmpDetails', methods=['GET'])
def name():
    DATABASE_URL = 'postgres://jqrebsheidydty:17058e8956a44769b277909cec6301ebb971bbb19c21dd8f0b00749115cbf57b@ec2-23-21-195-249.compute-1.amazonaws.com:5432/d716k7qsbfft4i'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    cursor.execute('select * from public."Employee"')
    data = cursor.fetchall()
    id=[]
#print(cursor.description)
    for record in data:
        print(record[0])
        id.append({'EmpId':record[0], 'EmpFirstName':record[1]})
    conn.close()
    return Response(json.dumps(id),  mimetype='application/json')
if __name__=="__main__":
    app.run(host='0.0.0.0', port='8081')
