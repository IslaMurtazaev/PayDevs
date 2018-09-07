import React from "react";
import { Link } from "react-router-dom";

const MonthlyRate = props => {
  return (
    <div>
      <Link
        to={`/project/${props.projectId}/Monthly/${
          props.monthPayment.id
        }/workedDay`}
      >
        <span className="rate">
          {props.monthPayment.rate}
          /per day
        </span>
      </Link>
      <button
        className="removeRate"
        onClick={() => props.onRemove(props.monthPayment.id)}
      >
        X
      </button>
    </div>
  );
};

export default MonthlyRate;
