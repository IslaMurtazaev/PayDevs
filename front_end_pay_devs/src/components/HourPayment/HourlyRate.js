import React from "react";
import { Link } from "react-router-dom";
import { history } from "../../index";

const HourPaymnetRate = props => {
  const { hourPayment, onRemove } = props;
  return (
    <div>
      <Link
        to={`${history.location.pathname}/Hourly/${hourPayment.id}/workTime`}
      >
        <span className="rate">
          {hourPayment.rate}
          /per hour _____
        </span>
      </Link>
      <button className="removeRate" onClick={() => onRemove(hourPayment.id)}>X</button>
    </div>
  );
};

export default HourPaymnetRate;
