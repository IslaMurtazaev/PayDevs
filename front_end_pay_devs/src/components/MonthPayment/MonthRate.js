import React from "react";
import { Link } from "react-router-dom";
import { history } from "../../index";

const MonthRate = props => {
  return (
    <div>
      <Link
        to={`${history.location.pathname}/Monthly/${props.id}/workedDays`}
      >
        <h3>{props.rate}</h3>
      </Link>
      <button onClick={() => props.onRemove(props.id)}>Remove rate</button>
    </div>
  );
};

export default MonthRate;
