import React, { useState } from 'react';
import axios from 'axios';

function SalesManagement() {
    const [productId, setProductId] = useState('');
    const [quantity, setQuantity] = useState('');
    const [createdDate, setCreatedDate] = useState('');
    const [saleRecord, setSaleRecord] = useState(null);

    const addSale = async () => {
        try {
            await axios.post('/api/sales', { product_id: productId, quantity: quantity, created_date: createdDate });
            setProductId('');
            setQuantity('');
            setCreatedDate('');
            alert('Sale record added successfully!');
        } catch (error) {
            alert('Error adding sale record.');
        }
    };

    const searchSale = async () => {
        try {
            const response = await axios.get(`/api/sales?product_id=${productId}`);
            setSaleRecord(response.data);
        } catch (error) {
            alert('Error searching sale record.');
        }
    };

    // Add similar functions for update and delete...

    return (
        <div>
            <h1>Sales Management</h1>
            
            <h2>Add New Sale Record</h2>
            <input value={productId} onChange={e => setProductId(e.target.value)} placeholder="Product ID" />
            <input value={quantity} onChange={e => setQuantity(e.target.value)} placeholder="Quantity" />
            <input type="date" value={createdDate} onChange={e => setCreatedDate(e.target.value)} placeholder="Created Date" />
            <button onClick={addSale}>Add Sale Record</button>

            <h2>Search Sale Record</h2>
            <input value={productId} onChange={e => setProductId(e.target.value)} placeholder="Product ID" />
            <button onClick={searchSale}>Search</button>

            {saleRecord && (
                <div>
                    <h2>Found Sale Record</h2>
                    <p>Product ID: {saleRecord.productId}</p>
                    <p>Quantity: {saleRecord.quantity}</p>
                    <p>Created Date: {saleRecord.createdDate}</p>
                    {/* Add buttons and functionality for update and delete here... */}
                </div>
            )}
        </div>
    );
}

export default SalesManagement;
