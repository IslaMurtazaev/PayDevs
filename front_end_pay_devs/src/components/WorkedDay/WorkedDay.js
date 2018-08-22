import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

import workedDayActions from "../../actions/workedDay";

const WorkedDay = props => {
  return (
    <div className="container">
      <span><b>Date:</b> {props.workedDay.day}</span>
      <span>{props.workedDay.paid || "not"} <b>paid</b></span>
      <Link className="button-group-horizontal"
        to={`/project/${props.projectId}/Monthly/${
          props.monthPaymentId
        }/workedDay/${props.workedDay.id}/update`}
      >
        <button>Update</button>
      </Link>
      <button onClick={props.removeWorkedDay}>Delete</button>
    </div> 
  );
};

const mapDispatchersToProps = (dispatch, ownProps) => ({
  removeWorkedDay: () =>
    dispatch(workedDayActions.remove(+ownProps.workedDay.id))
});

export default connect(
  null,
  mapDispatchersToProps
)(WorkedDay);
