from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

DATABASE = 'SalesRecord.db'

def query_db(query, args=(), one=False):
    with db.connect(DATABASE) as connection:
        cur = connection.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        connection.commit()
    return (rv[0] if rv else None) if one else rv

@app.route('/sales')
def sales():
    sales_records = query_db("SELECT * FROM SalesRecord")
    return render_template('sales.html', sales_records=sales_records)

@app.route('/add_sale', methods=['POST'])
def add_sale():
    """
    This function is used to add sales.
    """
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    created_date = request.form['created_date']
    
    query_db("INSERT INTO SalesRecord (productId, quantity, createdDate) VALUES (?, ?, ?)", (product_id, quantity, created_date))
    flash("Sale added successfully!")
    return redirect(url_for('sales'))

@app.route('/update_sale', methods=['POST'])
def update_sale():
    """
    This function is used to update sales.
    """
    sale_id = request.form['sale_id']
    new_product_id = request.form['new_product_id']
    new_quantity = request.form['new_quantity']
    new_created_date = request.form['new_created_date']
    
    query_db("UPDATE SalesRecord SET productId=?, quantity=?, createdDate=? WHERE id=?", (new_product_id, new_quantity, new_created_date, sale_id))
    flash("Sale updated successfully!")
    return redirect(url_for('sales'))

@app.route('/delete_sale', methods=['POST'])
def delete_sale():
    """
    This function is used to delete sales.
    """
    sale_id = request.form['sale_id']
    
    query_db("DELETE FROM SalesRecord WHERE id=?", (sale_id,))
    flash("Sale deleted successfully!")
    return redirect(url_for('sales'))

if __name__ == '__main__':
    app.run(debug=True)
