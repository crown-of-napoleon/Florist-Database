import React, { useState, useEffect } from "react";
import Footer from "./Footer";
import Header from "./Header";
import Note from "./Note";
import Area from "./Area";

function App() {
  const [notesArray, setNotesArray] = useState([]);

  // Fetch notes from the backend on component mount
  useEffect(() => {
    fetch("http://localhost:5001/api/notes")
      .then((response) => response.json())
      .then((data) => setNotesArray(data))
      .catch((err) => console.error("Error loading notes:", err));
  }, []);

  function addNote(newNote) {
    fetch("http://localhost:5001/api/notes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newNote),
    })
      .then((response) => response.json())
      .then((data) => {
        setNotesArray((prevNotes) => [...prevNotes, data]);
      })
      .catch((err) => console.error("Error adding note:", err));
  }

  function removeNote(id) {
    fetch(`http://localhost:5001/api/notes/${id}`, {
      method: "DELETE",
    })
      .then((response) => {
        if (response.ok) {
          setNotesArray((prevNotes) =>
            prevNotes.filter((note) => note._id !== id)
          );
        }
      })
      .catch((err) => console.error("Error removing note:", err));
  }

  function modifyQuantity(id, delta) {
    setNotesArray(prev => prev.map(note => {
      if (note._id === id) {
        const updatedQuantity = Math.max(0, note.quantity + delta);
        updateQuantity(id, updatedQuantity);
        return { ...note, quantity: updatedQuantity };
      }
      return note;
    }));
  }
  
  function updateQuantity(id, quantity) {
    fetch(`http://localhost:5001/api/notes/${id}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ quantity })
    })
    .then(response => response.json())
    .then(data => {
      console.log('Quantity updated:', data);
    })
    .catch(err => {
      console.error('Error updating quantity:', err);
      alert('Failed to update quantity.');
    });
  }

  return (
    <div>
      <Header />
      <Area onAdd={addNote} />
      {notesArray.map((note) => (
        <Note
          key={note._id}
          id={note._id}
          title={note.title}
          price={note.price} // Pass the price to the Note component
          quantity={note.quantity}
          content={note.content}
          onDelete={() => removeNote(note._id)}
          onIncrease={() => modifyQuantity(note._id, 1)}
          onDecrease={() => modifyQuantity(note._id, -1)}
        />
      ))}
      <Footer />
    </div>
  );
}

export default App;
