import React from "react";
import { Link } from "react-router-dom";
import { history } from "../../index";

const MonthRate = props => {
  return (
    <div>
      <Link to={`${history.location.pathname}/Monthly/${props.id}/workedDay`}>
        <span className="rate">
         <li> {props.rate}
          /per day
         </li>
        </span>
      </Link>
      <button className="removeRate" onClick={() => props.onRemove(props.id)}>Remove rate</button>
    </div>
  );
};

export default MonthRate;
