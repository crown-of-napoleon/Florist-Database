# Import Flask.
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

DATABASE = 'InventoryLog.db'

def query_db(query, args=(), one=False):
    with db.connect(DATABASE) as connection:
        cur = connection.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        connection.commit()
    return (rv[0] if rv else None) if one else rv

@app.route('/inventory')
def inventory():
    inventory_items = query_db("SELECT * FROM InventoryLog")
    return render_template('inventory.html', inventory_items=inventory_items)

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    created_date = request.form['created_date']
    
    query_db("INSERT INTO InventoryLog (productId, quantity, createdDate) VALUES (?, ?, ?)", (product_id, quantity, created_date))
    flash("Inventory added successfully!")
    return redirect(url_for('inventory'))

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    inventory_id = request.form['inventory_id']
    new_quantity = request.form['new_quantity']
    new_created_date = request.form['new_created_date']
    
    query_db("UPDATE InventoryLog SET quantity=?, createdDate=? WHERE id=?", (new_quantity, new_created_date, inventory_id))
    flash("Inventory updated successfully!")
    return redirect(url_for('inventory'))

@app.route('/delete_inventory', methods=['POST'])
def delete_inventory():
    inventory_id = request.form['inventory_id']
    
    query_db("DELETE FROM InventoryLog WHERE id=?", (inventory_id,))
    flash("Inventory deleted successfully!")
    return redirect(url_for('inventory'))

if __name__ == '__main__':
    app.run(debug=True)
