from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

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

if __name__ == '__main__':
    app.run(debug=True)




