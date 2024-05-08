import React from "react";

function Note(props) {
  return (
    <div className="note">
      <h1>{props.title}</h1>
      <p>{props.content}</p>
      <p>Price: ${props.price}</p> {/* Display the price */}
      <p>Quantity: ${props.quantity}</p>
      <button onClick={() => props.onDelete(props.id)}>DELETE</button>
    </div>
  );
}

export default Note;
