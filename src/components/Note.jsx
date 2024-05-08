import React from "react";


function Note(props) {
  return (
    <div className="note">
      <div className="note-content">
        <h1>{props.title}</h1>
        {/* <p>{props.content}</p> */}
      </div>
      <div className="note-info">
        <p>Price: ${props.price}</p>
        <p>{props.content}</p>
        <div className="quantity-controls">
          <button className="small-button" onClick={() => props.onDecrease(props.id)}>-</button>
          <span className="quantity-display">{props.quantity}</span>
          <button className="small-button" onClick={() => props.onIncrease(props.id)}>+</button>
        </div>
      </div>
      <div className="note-actions">
        <button className="delete-button" onClick={() => props.onDelete(props.id)}>DELETE</button>
      </div>
    </div>
  );
}

export default Note;
