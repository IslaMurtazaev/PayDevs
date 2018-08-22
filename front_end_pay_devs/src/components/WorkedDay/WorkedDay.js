import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

import workedDayActions from "../../actions/workedDay";

const WorkedDay = props => {
  return (
    <div className="worked">
      <span><b>Date:</b> {props.workedDay.day}</span>
      <span>{props.workedDay.paid || "not"} <b>paid</b></span>
      <div className="button-group-horizontal">
       <Link 
        to={`/project/${props.projectId}/Monthly/${
          props.monthPaymentId
        }/workedDay/${props.workedDay.id}/update`}
       >
        <button className="updateButton btn btn-warning" type="button">Update</button>
       </Link>
       <button type="button" className="btn btn-danger" onClick={props.removeWorkedDay}>Delete</button>
      </div>
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
