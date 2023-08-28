import React, { useState } from 'react';
import axios from 'axios';

function CustomerManagement() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [customer, setCustomer] = useState(null);
    const [message, setMessage] = useState('');

    const handleAddCustomer = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/add_customer', { first_name: firstName, last_name: lastName });
            setMessage(response.data.message);
            setFirstName('');
            setLastName('');
        } catch (error) {
            setMessage('Error adding customer.');
        }
    };

    const handleSearchCustomer = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/search_customer', { search_first_name: firstName, search_last_name: lastName });
            if (response.data.customer) {
                setCustomer(response.data.customer);
            } else {
                setMessage('Customer not found.');
            }
        } catch (error) {
            setMessage('Error searching for customer.');
        }
    };

    const handleDeleteCustomer = async (customerId) => {
        try {
            const response = await axios.post('/delete_customer', { customer_id: customerId });
            setMessage(response.data.message);
            setCustomer(null);
        } catch (error) {
            setMessage('Error deleting customer.');
        }
    };

    const handleUpdateCustomer = async (customerId, updatedFirstName, updatedLastName) => {
        try {
            const response = await axios.post('/update_customer', {
                update_customer_id: customerId,
                update_first_name: updatedFirstName,
                update_last_name: updatedLastName
            });
            setMessage(response.data.message);
            setCustomer(response.data.updatedCustomer);
        } catch (error) {
            setMessage('Error updating customer.');
        }
    };

    return (
        <div className="container mt-5">
            <h1 className="mb-4">Customer Management</h1>

            {message && <div className="alert alert-info">{message}</div>}

            <div className="mb-4">
                <h2>Add New Customer</h2>
                <form onSubmit={handleAddCustomer}>
                    <div className="form-group">
                        <label htmlFor="first_name">First Name:</label>
                        <input type="text" className="form-control" id="first_name" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="last_name">Last Name:</label>
                        <input type="text" className="form-control" id="last_name" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                    </div>
                    <button type="submit" className="btn btn-primary">Add Customer</button>
                </form>
            </div>

            <div className="mb-4">
                <h2>Search Customer</h2>
                <form onSubmit={handleSearchCustomer}>
                    <div className="form-group">
                        <label htmlFor="search_first_name">First Name:</label>
                        <input type="text" className="form-control" id="search_first_name" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="search_last_name">Last Name:</label>
                        <input type="text" className="form-control" id="search_last_name" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                    </div>
                    <button type="submit" className="btn btn-info">Search</button>
                </form>
            </div>

            {customer && (
                <div className="mb-4">
                    <h2>Found Customer</h2>
                    <p>First Name: {customer.firstName}</p>
                    <p>Last Name: {customer.lastName}</p>
                    <button className="btn btn-danger" onClick={() => handleDeleteCustomer(customer.id)}>Delete</button>
                    <form onSubmit={() => handleUpdateCustomer(customer.id, firstName, lastName)}>
                        <div className="form-group">
                            <label htmlFor="update_first_name">Update First Name:</label>
                            <input type="text" className="form-control" id="update_first_name" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                        </div>
                        <div className="form-group">
                            <label htmlFor="update_last_name">Update Last Name:</label>
                            <input type="text" className="form-control" id="update_last_name" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                        </div>
                        <button type="submit" className="btn btn-warning">Update</button>
                    </form>
                </div>
            )}
        </div>
    );
}

export default CustomerManagement;
