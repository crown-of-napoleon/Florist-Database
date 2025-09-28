import React, { useState } from "react";

function Note(props) {
  const [isEditing, setIsEditing] = useState(false);
  const [newContent, setNewContent] = useState(props.content);
  const [newPrice, setNewPrice] = useState(props.price);

  const handleSave = () => {
    // Call the parent function to update both content and price
    props.onUpdate(props.id, { content: newContent, price: parseFloat(newPrice) });
    setIsEditing(false);
  };

  const handleCancel = () => {
    // Reset to original values
    setNewContent(props.content);
    setNewPrice(props.price);
    setIsEditing(false);
  };

  return (
    <div className="note">
      <div className="note-content">
        <h1>{props.title}</h1>
      </div>
      <div className="note-info">
        {/* Price editor */}
        {isEditing ? (
          <div className="price-editor">
            <label>Price: $</label>
            <input
              type="number"
              step="0.01"
              min="0"
              className="edit-price"
              value={newPrice}
              onChange={(e) => setNewPrice(e.target.value)}
            />
          </div>
        ) : (
          <p>Price: ${props.price}</p>
        )}

        {/* Description editor */}
        {isEditing ? (
          <textarea
            className="edit-description"
            value={newContent}
            onChange={(e) => setNewContent(e.target.value)}
            placeholder="Enter description..."
          />
        ) : (
          <p>{props.content || "No description"}</p>
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
          <>
            <button className="save-button" onClick={handleSave}>
              SAVE
            </button>
            <button className="cancel-button" onClick={handleCancel}>
              CANCEL
            </button>
          </>
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