import React from 'react';

const WorkedDay = props => {
  return (
    <div className="container">
      <h5>Date: {props.workedDay.day}</h5>
      <h5>{props.workedDay.paid || "not"} paid</h5>
    </div>
  );
}
 
export default WorkedDay;
