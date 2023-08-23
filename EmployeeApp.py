from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

DATABASE = 'your_database_name.db'  # Replace with the name of your SQLite database

def query_db(query, args=(), one=False):
    con = db.connect(DATABASE)
    cur = con.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    con.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee')
def employee():
    employees = query_db("SELECT * FROM Employee")
    return render_template('employee.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    position = request.form['position']
    query = "INSERT INTO Employee (firstName, lastName, position) VALUES (?, ?, ?)"
    query_db(query, (first_name, last_name, position))
    flash("Employee added successfully!")
    return redirect(url_for('employee'))

@app.route('/update_employee', methods=['POST'])
def update_employee():
    employee_id = request.form['employee_id']
    new_first_name = request.form['new_first_name']
    new_last_name = request.form['new_last_name']
    new_position = request.form['new_position']
    query = "UPDATE Employee SET firstName=?, lastName=?, position=? WHERE id=?"
    query_db(query, (new_first_name, new_last_name, new_position, employee_id))
    flash("Employee updated successfully!")
    return redirect(url_for('employee'))

@app.route('/delete_employee', methods=['POST'])
def delete_employee():
    employee_id = request.form['employee_id']
    query = "DELETE FROM Employee WHERE id=?"
    query_db(query, (employee_id,))
    flash("Employee deleted successfully!")
    return redirect(url_for('employee'))

if __name__ == '__main__':
    app.run(debug=True)
