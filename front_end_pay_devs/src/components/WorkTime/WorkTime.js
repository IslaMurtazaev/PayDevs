import React from "react";
import { Link } from "react-router-dom";

const WorkTimeItem = props => {
  const { projectId, hourPaymentId, workTime, onRemove } = props;
  return (
    <div className="container">
      <h5>Start Work: {new Date(workTime.start_work).toLocaleString()}</h5>
      <h5>End Work: {new Date(workTime.end_work).toLocaleString()}</h5>
      <h5>{workTime.paid || "not"} paid</h5>
      <Link
        to={`/project/${projectId}/Hourly/${hourPaymentId}/workTime/${
          workTime.id
        }/update`}
      >
        <button>Update</button>
      </Link>
      <button onClick={() => onRemove(workTime.id)}>Delete</button>
    </div>
  );
};

export default WorkTimeItem;
