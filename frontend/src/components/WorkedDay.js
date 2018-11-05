import React from "react";
import { Link } from "react-router-dom";

const WorkedDay = props => {
  const { workedDay, projectId, monthPaymentId, onRemove } = props;

  return (
    <div className="worked">
      <h4 className="date">
        <b>Date:</b> {workedDay.day}
      </h4>
      <h4 className="paid">
        {workedDay.paid || "not "}
        <b>paid</b>
      </h4>
      <div className="button-group-horizontal">
        <Link
          to={`/project/${projectId}/Monthly/${monthPaymentId}/workedDay/${
            workedDay.id
          }/update`}
        >
          <button
            className="updateButton btn btn-warning updateWorkedDay"
            type="button"
          >
            Update
          </button>
        </Link>
        <button
          type="button"
          className="btn btn-danger removeWorkDay"
          onClick={() => onRemove(workedDay.id)}
        >
          Delete
        </button>
      </div>
    </div>
  );
};

export default WorkedDay;
