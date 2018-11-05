import React from "react";
import { connect } from "react-redux";

import FormikWorkTime from "../forms/FormikWorkTime";
import workTimeActions from "../actions/workTime";

const UpdateWorkTimeForm = props => {
  return (
    <div>
      <h2>Update Work Time</h2>
      <FormikWorkTime
        id={props.workTime.id}
        start_work={props.workTime.start_work}
        end_work={props.workTime.end_work}
        paid={props.workTime.paid}
        onSubmit={values => props.updateWorkTime(values)}
      />
    </div>
  );
};

const mapStateToProps = (state, ownProps) => ({
  workTime: state.workTimes.find(
    workTime => workTime.id === +ownProps.match.params.workTimeId
  )
});

const mapDispatchToProps = (dispatch, ownProps) => ({
  updateWorkTime: values =>
    dispatch(
      workTimeActions.update(
        +ownProps.match.params.id,
        +ownProps.match.params.hourPaymentId,
        values.id,
        values
      )
    )
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UpdateWorkTimeForm);
