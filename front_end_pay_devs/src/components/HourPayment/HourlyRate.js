import React from "react";
import { Link } from "react-router-dom";
import { history } from "../../index";

const HourlyRate = props => {
  const { hourPayment, onRemove } = props;

  return (
    <div>
      <Link
        to={`${history.location.pathname}/Hourly/${hourPayment.id}/workTime`}
        className="workTimes"
      >
        <span className="rate">
          {hourPayment.rate}
          /per hour
        </span>
      </Link>
      <button className="removeRate" onClick={() => onRemove(hourPayment.id)}>
        X
      </button>
    </div>
  );
};

export default HourlyRate;
