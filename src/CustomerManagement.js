import React, { useState } from 'react';
import axios from 'axios';
import 'static/css/CustomerManagement.css'

function CustomerManagement({ initialData }) {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [customer, setCustomer] = useState(initialData);

    const addCustomer = async () => {
        try {
            await axios.post('/api/customer', { first_name: firstName, last_name: lastName });
            setFirstName('');
            setLastName('');
            alert('Customer added successfully!');
        } catch (error) {
            alert('Error adding customer.');
        }
    };

    const searchCustomer = async () => {
        try {
            const response = await axios.get(`/api/customer?first_name=${firstName}&last_name=${lastName}`);
            setCustomer(response.data);
        } catch (error) {
            alert('Error searching customer.');
        }
    };

    // Add similar functions for update and delete...

    return (
        <div>
            <h1>Customer Management</h1>
            
            <h2>Add New Customer</h2>
            <input value={firstName} onChange={e => setFirstName(e.target.value)} placeholder="First Name" />
            <input value={lastName} onChange={e => setLastName(e.target.value)} placeholder="Last Name" />
            <button onClick={addCustomer}>Add Customer</button>

            <h2>Search Customer</h2>
            <input value={firstName} onChange={e => setFirstName(e.target.value)} placeholder="First Name" />
            <input value={lastName} onChange={e => setLastName(e.target.value)} placeholder="Last Name" />
            <button onClick={searchCustomer}>Search</button>

            {customer && (
                <div>
                    <h2>Found Customer</h2>
                    <p>First Name: {customer.firstName}</p>
                    <p>Last Name: {customer.lastName}</p>
                    {/* Add buttons and functionality for update and delete here... */}
                </div>
            )}
        </div>
    );
}

export default CustomerManagement;
