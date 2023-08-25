from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Api, Resource
import sqlite3 as db

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
    return render_template('index.html')

@app.route('/add_customer', methods=['POST'])
def add_customer():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    connection = db.connect('customer.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Customer (firstName, lastName) VALUES (?, ?)", (first_name, last_name))
    connection.commit()
    connection.close()
    flash("Customer added successfully!")
    return redirect(url_for('index'))

@app.route('/search_customer', methods=['POST'])
def search_customer():
    first_name = request.form['search_first_name']
    last_name = request.form['search_last_name']
    connection = db.connect('customer.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customer WHERE firstName=? AND lastName=?", (first_name, last_name))
    customer = cursor.fetchone()
    connection.close()
    if customer:
        return render_template('index.html', customer=customer)
    else:
        flash("Customer not found!")
        return redirect(url_for('index'))

@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    customer_id = request.form['customer_id']
    connection = db.connect('customer.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Customer WHERE id=?", (customer_id,))
    connection.commit()
    connection.close()
    flash("Customer deleted successfully!")
    return redirect(url_for('index'))

@app.route('/update_customer', methods=['POST'])
def update_customer():
    customer_id = request.form['update_customer_id']
    new_first_name = request.form['update_first_name']
    new_last_name = request.form['update_last_name']
    connection = db.connect('customer.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE Customer SET firstName=?, lastName=? WHERE id=?", (new_first_name, new_last_name, customer_id))
    connection.commit()
    connection.close()
    flash("Customer updated successfully!")
    return redirect(url_for('index'))

class CustomerResource(Resource):
    def get(self, customer_id=None):
        connection = db.connect('customer.db')
        cursor = connection.cursor()
        if customer_id:
            cursor.execute("SELECT * FROM Customer WHERE id=?", (customer_id,))
            customer = cursor.fetchone()
            connection.close()
            if customer:
                return {"customer": customer}
            else:
                return {"message": "Customer not found"}, 404
        else:
            cursor.execute("SELECT * FROM Customer")
            customers = cursor.fetchall()
            connection.close()
            return {"customers": customers}

    def post(self):
        # This is similar to your add_customer function
        # Extract details from request and add to the database
        pass

    def put(self, customer_id):
        # This is similar to your update_customer function
        # Extract details from request and update the database record
        pass

    def delete(self, customer_id):
        # This is similar to your delete_customer function
        # Delete the customer from the database
        pass

api.add_resource(CustomerResource, '/api/customer', '/api/customer/<int:customer_id>')


if __name__ == '__main__':
    app.run(debug=True)




