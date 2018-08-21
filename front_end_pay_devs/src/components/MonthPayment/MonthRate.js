import React from "react";
import { Link } from "react-router-dom";
import { history } from "../../index";

const MonthRate = props => {
  return (
    <div>
      <Link to={`${history.location.pathname}/Monthly/${props.id}/workedDay`}>
        <span className="rate">
          {props.rate}
          /per day _____
        </span>
      </Link>
      <button className="removeRate" onClick={() => props.onRemove(props.id)}>X</button>
    </div>
  );
};

export default MonthRate;
