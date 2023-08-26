import React, { useState } from 'react';
import axios from 'axios';

function InventoryManagement() {
    const [productId, setProductId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [createdDate, setCreatedDate] = useState('');
    const [inventoryItem, setInventoryItem] = useState(null);

    const addInventory = async () => {
        try {
            await axios.post('/api/inventory', { product_id: productId, quantity: quantity, created_date: createdDate });
            setProductId('');
            setQuantity('');
            setCreatedDate('');
            alert('Inventory item added successfully!');
        } catch (error) {
            alert('Error adding inventory item.');
        }
    };

    const searchInventory = async () => {
        try {
            const response = await axios.get(`/api/inventory?product_id=${productId}`);
            setInventoryItem(response.data);
        } catch (error) {
            alert('Error searching inventory item.');
        }
    };

    // Add similar functions for update and delete...

    return (
        <div>
            <h1>Inventory Management</h1>
            
            <h2>Add New Inventory Item</h2>
            <input value={productId} onChange={e => setProductId(e.target.value)} placeholder="Product ID" />
            <input value={quantity} onChange={e => setQuantity(e.target.value)} placeholder="Quantity" />
            <input type="date" value={createdDate} onChange={e => setCreatedDate(e.target.value)} placeholder="Created Date" />
            <button onClick={addInventory}>Add Inventory Item</button>

            <h2>Search Inventory Item</h2>
            <input value={productId} onChange={e => setProductId(e.target.value)} placeholder="Product ID" />
            <button onClick={searchInventory}>Search</button>

            {inventoryItem && (
                <div>
                    <h2>Found Inventory Item</h2>
                    <p>Product ID: {inventoryItem.productId}</p>
                    <p>Quantity: {inventoryItem.quantity}</p>
                    <p>Created Date: {inventoryItem.createdDate}</p>
                    {/* Add buttons and functionality for update and delete here... */}
                </div>
            )}
        </div>
    );
}

export default InventoryManagement;
