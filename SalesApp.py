from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

DATABASE = 'SalesRecord.db'  # This is based on the provided code

@app.route('/sales')
def sales():
    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM SalesRecord")
    sales_records = cursor.fetchall()
    connection.close()
    return render_template('sales.html', sales_records=sales_records)

@app.route('/add_sale', methods=['POST'])
def add_sale():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    created_date = request.form['created_date']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO SalesRecord (productId, quantity, createdDate) VALUES (?, ?, ?)", (product_id, quantity, created_date))
    connection.commit()
    connection.close()

    flash("Sale added successfully!")
    return redirect(url_for('sales'))

@app.route('/update_sale', methods=['POST'])
def update_sale():
    sale_id = request.form['sale_id']
    new_product_id = request.form['new_product_id']
    new_quantity = request.form['new_quantity']
    new_created_date = request.form['new_created_date']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("UPDATE SalesRecord SET productId=?, quantity=?, createdDate=? WHERE id=?", (new_product_id, new_quantity, new_created_date, sale_id))
    connection.commit()
    connection.close()

    flash("Sale updated successfully!")
    return redirect(url_for('sales'))

@app.route('/delete_sale', methods=['POST'])
def delete_sale():
    sale_id = request.form['sale_id']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM SalesRecord WHERE id=?", (sale_id,))
    connection.commit()
    connection.close()

    flash("Sale deleted successfully!")
    return redirect(url_for('sales'))

if __name__ == '__main__':
    app.run(debug=True)
