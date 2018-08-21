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
        <h3>
          {hourPayment.rate}
          /per hour
        </h3>
      </Link>
      <button onClick={() => onRemove(hourPayment.id)}>Remove rate</button>
    </div>
  );
};

export default HourPaymnetRate;
