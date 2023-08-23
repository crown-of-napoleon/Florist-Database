from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as db

app = Flask(__name__)
app.secret_key = "florist_secret_key"

DATABASE = 'SalesRecord.db'  # This is based on the provided code

@app.route('/inventory')
def inventory():
    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM InventoryLog")
    inventory_items = cursor.fetchall()
    connection.close()
    return render_template('inventory.html', inventory_items=inventory_items)

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    product_id = request.form['product_id']
    quantity = request.form['quantity']
    created_date = request.form['created_date']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO InventoryLog (productId, quantity, createdDate) VALUES (?, ?, ?)", (product_id, quantity, created_date))
    connection.commit()
    connection.close()

    flash("Inventory added successfully!")
    return redirect(url_for('inventory'))

@app.route('/update_inventory', methods=['POST'])
def update_inventory():
    inventory_id = request.form['inventory_id']
    new_quantity = request.form['new_quantity']
    new_created_date = request.form['new_created_date']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("UPDATE InventoryLog SET quantity=?, createdDate=? WHERE id=?", (new_quantity, new_created_date, inventory_id))
    connection.commit()
    connection.close()

    flash("Inventory updated successfully!")
    return redirect(url_for('inventory'))

@app.route('/delete_inventory', methods=['POST'])
def delete_inventory():
    inventory_id = request.form['inventory_id']

    connection = db.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM InventoryLog WHERE id=?", (inventory_id,))
    connection.commit()
    connection.close()

    flash("Inventory deleted successfully!")
    return redirect(url_for('inventory'))

if __name__ == '__main__':
    app.run(debug=True)
