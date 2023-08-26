from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Api, Resource, reqparse
import sqlite3 as db

# Set up the Flask app and the API
app = Flask(__name__)
api = Api(app)
app.secret_key = "florist_secret_key"

def query_db(query, args=(), one=False):
    """
    This function is used to query the database.
    """
    with db.connect('customer.db') as connection:
        cur = connection.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        connection.commit()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    """
    This function is used to render the index.html template.
    """
    return render_template('index.html')

class CustomerResource(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', type=str, required=True, help="First name cannot be blank!")
    parser.add_argument('last_name', type=str, required=True, help="Last name cannot be blank!")

    def get(self, customer_id=None):
        """
        This function is used to get a customer from the database.
        """
        if customer_id:
            customer = query_db("SELECT * FROM Customer WHERE id=?", (customer_id,), one=True)
            if customer:
                return {"customer": customer}
            else:
                return {"message": "Customer not found"}, 404
        else:
            customers = query_db("SELECT * FROM Customer")
            return {"customers": customers}

    def post(self):
        args = self.parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']
        
        query_db("INSERT INTO Customer (firstName, lastName) VALUES (?, ?)", (first_name, last_name))
        return {"message": "Customer added successfully!"}, 201

    def put(self, customer_id):
        args = self.parser.parse_args()
        new_first_name = args['first_name']
        new_last_name = args['last_name']
        
        query_db("UPDATE Customer SET firstName=?, lastName=? WHERE id=?", (new_first_name, new_last_name, customer_id))
        return {"message": "Customer updated successfully!"}

    def delete(self, customer_id):
        query_db("DELETE FROM Customer WHERE id=?", (customer_id,))
        return {"message": "Customer deleted successfully!"}

api.add_resource(CustomerResource, '/api/customer', '/api/customer/<int:customer_id>')

if __name__ == '__main__':
    app.run(debug=True)
