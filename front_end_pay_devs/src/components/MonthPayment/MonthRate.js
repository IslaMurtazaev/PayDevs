import React from "react";

const MonthRate = props => {
  return (
    <div>
      <h3>{props.rate}</h3>
      <button onClick={() => props.onRemove(props.id)}>Remove rate</button>
    </div>
  );
};

export default MonthRate;
