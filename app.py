
from flask import Flask, Flask, flash, render_template, url_for, session, jsonify, redirect, send_from_directory
import os
import logging
import urllib.request
import flask
from flask import request
from werkzeug.utils import secure_filename
import time 
import mysql.connector 

conn = mysql.connector.connect(user='root', password='indianit16',
                              host='localhost',
                              database='hrms',
                              auth_plugin='mysql_native_password')



app = Flask(__name__)


users = {}

# server = '127.0.0.1:3306' 
# database = 'hrms' 
# username = 'root' 
# password = 'indianit16' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()


# #database connection
# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                     'Server=localhost;'
#                     'PORT=3306;'
#                     'Database=hrms;'
#                     'UID=root;'
#                     'PWD=indianit16;')


@app.route('/addEmployee', methods=['POST'])
def add_emp():
    emp_name = request.values.get('emp_name', None)
    salary = request.values.get('salary', None)
    hr_id = request.values.get('hr_id', None)
    cursor = conn.cursor()
    sql = "insert into Employee(emp_name, salary, hr_id) values (%s, %s, %s)"
    val = (emp_name, salary, hr_id)
    cursor.execute(sql, val)
    conn.commit()
    if cursor.rowcount > 0:
        result = 'Added a new employee successfully'
    # cursor.execute("SELECT id, Firstname, lastname FROM DB_EnspireMock.dbo.HRMS_EMP_MASTER WITH (NOLOCK) WHERE status = ?", 1 )
    return jsonify(cursor.rowcount)
    

@app.route('/DeleteEmployee', methods=['POST'])
def del_emp():
    emp_id = request.values.get('emp_id', None)
    salary = request.values.get('salary', None)
    hr_id = request.values.get('hr_id', None)
    cursor = conn.cursor()
    sql = "DELETE FROM Employee WHERE id = %s"
    employee_id = (emp_id, )
    cursor.execute(sql, employee_id)
    conn.commit()
    if cursor.rowcount > 0:
        result = 'Deleted Successfully'
    # cursor.execute("SELECT id, Firstname, lastname FROM DB_EnspireMock.dbo.HRMS_EMP_MASTER WITH (NOLOCK) WHERE status = ?", 1 )
    return jsonify(cursor.rowcount)
    

@app.route('/UpdateEmployee', methods=['PUT'])
def update_emp():
    emp_name = request.values.get('emp_name', None)
    salary = request.values.get('salary', None)
    emp_id = request.values.get('emp_id', None)
    cursor = conn.cursor()
    cursor.execute("UPDATE Employee SET emp_name=%s, salary=%s WHERE id=%s", (emp_name,salary, emp_id))
    conn.commit()
    # cursor.execute("SELECT id, Firstname, lastname FROM DB_EnspireMock.dbo.HRMS_EMP_MASTER WITH (NOLOCK) WHERE status = ?", 1 )
    return jsonify(cursor.rowcount)


@app.route('/login', methods=['POST'])
def get_id2():
    userid = request.values.get('userid', None)
    password = request.values.get('pass', None)
    cursor = conn.cursor()
    sql = "SELECT id, FirstName, LastName FROM HR WHERE username =%s and pass = %s"
    # cursor.execute("SELECT id, FirstName, LastName FROM HR WHERE username =%s and pass = %s", userid, password)
    adr = (userid, password, )
    cursor.execute(sql, (adr))
    myresult = cursor.fetchall()
    if myresult[0]!= 'null':
        hr_id = myresult[0][0]
        user_data = GetUser(hr_id)
    else:
        print('Not an HR')
    return jsonify(user_data)


def GetUser(hr_id):
    cursor = conn.cursor()
    sql = "SELECT * FROM Employee WHERE hr_id =%s"
    adr = (hr_id, )
    cursor.execute(sql, adr)
    employee = cursor.fetchall()
    return employee

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


if __name__ == '__main__':
    app.run(app, host= '0.0.0.0', debug=True, port=8081)