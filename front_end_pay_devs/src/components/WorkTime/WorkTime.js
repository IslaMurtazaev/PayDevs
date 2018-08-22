import React from "react";
import { Link } from "react-router-dom";

const WorkTimeItem = props => {
  const { projectId, hourPaymentId, workTime, onRemove } = props;
  return (
    <div className="workedTime">
      <h4><b>Start Work:</b> {new Date(workTime.start_work).toLocaleString()} </h4>
      <h4><b>End Work:</b> {new Date(workTime.end_work).toLocaleString()}</h4>
      <h4>{workTime.paid || "not"} <b>paid</b></h4>
      <div className="button-group-horizontal">
      <Link 
        to={`/project/${projectId}/Hourly/${hourPaymentId}/workTime/${
          workTime.id
        }/update`}  
      >
        <button className="updateButton btn btn-warning" type="button">Update</button>
      </Link>
      <button type="button" className="btn btn-danger" onClick={() => onRemove(workTime.id)}>Delete</button>
      </div>
         </div> 
  );
};

export default WorkTimeItem;
