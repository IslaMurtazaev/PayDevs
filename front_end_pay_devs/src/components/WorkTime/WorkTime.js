import React from "react";
import { Link } from "react-router-dom";

const WorkTimeItem = props => {
  const { projectId, hourPaymentId, workTime, onRemove } = props;
  return (
    <div className="container">
    <li>
      <span><b>Start Work:</b> {new Date(workTime.start_work).toLocaleString()} </span>
      <span><b>End Work:</b> {new Date(workTime.end_work).toLocaleString()}</span>
      <span>{workTime.paid || "not"} <b>paid</b></span>
      <Link className="button-group-horizontal"
        to={`/project/${projectId}/Hourly/${hourPaymentId}/workTime/${
          workTime.id
        }/update`}  
      >
        <button>Update</button>
      </Link>
      <button onClick={() => onRemove(workTime.id)}>Delete</button>
      </li>
    </div> 
  );
};

export default WorkTimeItem;
