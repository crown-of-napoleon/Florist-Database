from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_restful import Api, Resource, reqparse
import sqlite3 as db

app = Flask(__name__)
api = Api(app)
app.secret_key = "florist_secret_key"

DATABASE = 'your_database_name.db'  # Replace with the name of your SQLite database

def query_db(query, args=(), one=False):
    with db.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        con.commit()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    return render_template('index.html')

class EmployeeResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True, help="First name cannot be blank!")
    parser.add_argument('last_name', type=str, required=True, help="Last name cannot be blank!")
    parser.add_argument('position', type=str, required=True, help="Position cannot be blank!")

    def get(self, employee_id=None):
        if employee_id:
            employee = query_db("SELECT * FROM Employee WHERE id=?", (employee_id,), one=True)
            if employee:
                return {"employee": employee}
            else:
                return {"message": "Employee not found"}, 404
        else:
            employees = query_db("SELECT * FROM Employee")
            return {"employees": employees}

    def post(self):
        args = self.parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']
        position = args['position']
        
        query_db("INSERT INTO Employee (firstName, lastName, position) VALUES (?, ?, ?)", (first_name, last_name, position))
        return {"message": "Employee added successfully!"}, 201

    def put(self, employee_id):
        args = self.parser.parse_args()
        new_first_name = args['first_name']
        new_last_name = args['last_name']
        new_position = args['position']
        
        query_db("UPDATE Employee SET firstName=?, lastName=?, position=? WHERE id=?", (new_first_name, new_last_name, new_position, employee_id))
        return {"message": "Employee updated successfully!"}

    def delete(self, employee_id):
        query_db("DELETE FROM Employee WHERE id=?", (employee_id,))
        return {"message": "Employee deleted successfully!"}

api.add_resource(EmployeeResource, '/api/employee', '/api/employee/<int:employee_id>')

if __name__ == '__main__':
    app.run(debug=True)
