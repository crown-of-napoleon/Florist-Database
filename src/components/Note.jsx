import React, { useState } from "react";

function Note(props) {
  const [isEditing, setIsEditing] = useState(false);
  const [newContent, setNewContent] = useState(props.content);

  const handleSave = () => {
    props.onUpdateContent(props.id, newContent); // Call the parent function to update content
    setIsEditing(false);
  };

  return (
    <div className="note">
      <div className="note-content">
        <h1>{props.title}</h1>
      </div>
      <div className="note-info">
        <p>Price: ${props.price}</p>
        {/* Description editor */}
        {isEditing ? (
          <textarea
            className="edit-description"
            value={newContent}
            onChange={(e) => setNewContent(e.target.value)}
          />
        ) : (
          <p>{props.content}</p>
        )}
        <div className="quantity-controls">
          <button
            className="small-button"
            onClick={() => props.onDecrease(props.id)}
          >
            -
          </button>
          <span className="quantity-display">{props.quantity}</span>
          <button
            className="small-button"
            onClick={() => props.onIncrease(props.id)}
          >
            +
          </button>
        </div>
      </div>
      <div className="note-actions">
        <button
          className="delete-button"
          onClick={() => props.onDelete(props.id)}
        >
          DELETE
        </button>
        {isEditing ? (
          <button className="save-button" onClick={handleSave}>
            SAVE
          </button>
        ) : (
          <button
            className="edit-button"
            onClick={() => setIsEditing(true)}
          >
            EDIT
          </button>
        )}
      </div>
    </div>
  );
}

export default Note;