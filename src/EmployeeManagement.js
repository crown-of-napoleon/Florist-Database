// Import React
import React, { useState } from 'react';
import axios from 'axios';

function EmployeeManagement() {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [position, setPosition] = useState('');
    const [employee, setEmployee] = useState(null);

    const addEmployee = async () => {
        try {
            await axios.post('/api/employee', { first_name: firstName, last_name: lastName, position: position });
            setFirstName('');
            setLastName('');
            setPosition('');
            alert('Employee added successfully!');
        } catch (error) {
            alert('Error adding employee.');
        }
    };

    const searchEmployee = async () => {
        try {
            const response = await axios.get(`/api/employee?first_name=${firstName}&last_name=${lastName}`);
            setEmployee(response.data);
        } catch (error) {
            alert('Error searching employee.');
        }
    };

    // Add similar functions for update and delete...

    return (
        <div>
            <h1>Employee Management</h1>
            
            <h2>Add New Employee</h2>
            <input value={firstName} onChange={e => setFirstName(e.target.value)} placeholder="First Name" />
            <input value={lastName} onChange={e => setLastName(e.target.value)} placeholder="Last Name" />
            <input value={position} onChange={e => setPosition(e.target.value)} placeholder="Position" />
            <button onClick={addEmployee}>Add Employee</button>

            <h2>Search Employee</h2>
            <input value={firstName} onChange={e => setFirstName(e.target.value)} placeholder="First Name" />
            <input value={lastName} onChange={e => setLastName(e.target.value)} placeholder="Last Name" />
            <button onClick={searchEmployee}>Search</button>

            {employee && (
                <div>
                    <h2>Found Employee</h2>
                    <p>First Name: {employee.firstName}</p>
                    <p>Last Name: {employee.lastName}</p>
                    <p>Position: {employee.position}</p>
                    {/* Add buttons and functionality for update and delete here... */}
                </div>
            )}
        </div>
    );
}

export default EmployeeManagement;
