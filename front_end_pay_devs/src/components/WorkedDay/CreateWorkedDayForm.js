import React from "react";
import { connect } from "react-redux";

import FormikWorkedDay from "../../forms/FormikWorkedDay";
import workedDayActions from "../../actions/workedDay";

const CreateWorkedDayForm = props => {
  return (
    <div>
      <h1>Create Worked Day</h1>
      <FormikWorkedDay onSubmit={props.createWorkedDay} />
    </div>
  );
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    createWorkedDay: values =>
      dispatch(
        workedDayActions.create(
          +ownProps.match.params.id,
          +ownProps.match.params.monthPaymentId,
          values
        )
      )
  };
};

export default connect(
  null,
  mapDispatchToProps
)(CreateWorkedDayForm);
