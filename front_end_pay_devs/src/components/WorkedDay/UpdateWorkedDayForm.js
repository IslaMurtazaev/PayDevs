import React from "react";
import { connect } from "react-redux";

import FormikWorkedDay from "../../forms/FormikWorkedDay";
import workedDayActions from "../../actions/workedDay";

const UpdateWorkedDayForm = props => {
  return (
    <div>
      <h1>Update Worked Day</h1>
      <FormikWorkedDay
        id={props.workedDay.id}
        day={props.workedDay.day}
        paid={props.workedDay.paid}
        onSubmit={values => props.updateWorkedDay(values)}
      />
    </div>
  );
};

const mapStateToProps = (state, ownProps) => ({
  workedDay: state.workedDays.find(
    workedDay => workedDay.id === +ownProps.match.params.workedDayId
  )
});

const mapDispatchToProps = (dispatch, ownProps) => ({
  updateWorkedDay: values =>
    dispatch(
      workedDayActions.update(
        +ownProps.match.params.id,
        +ownProps.match.params.monthPaymentId,
        values.id,
        values
      )
    )
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UpdateWorkedDayForm);
