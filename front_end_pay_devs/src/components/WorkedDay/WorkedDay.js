import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

import workedDayActions from "../../actions/workedDay";

const WorkedDay = props => {
  return (
    <div className="worked">
      <h4><b>Date:</b> {props.workedDay.day}</h4>
      <h4>{props.workedDay.paid || "not"} <b>paid</b></h4>
      <div className="button-group-horizontal">
       <Link 
        to={`/project/${props.projectId}/Monthly/${
          props.monthPaymentId
        }/workedDay/${props.workedDay.id}/update`}
       >
        <button className="updateButton btn btn-warning" type="button">Update</button>
       </Link>
       <button type="button" className="deleteButton btn btn-danger" onClick={props.removeWorkedDay}>Delete</button>
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
