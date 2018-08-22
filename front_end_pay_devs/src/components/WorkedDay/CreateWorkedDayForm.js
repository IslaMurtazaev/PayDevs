import React from "react";
import { connect } from "react-redux";

import FormikWorkedDay from "../../forms/FormikWorkedDay";
import workedDayActions from "../../actions/workedDay";

const CreateWorkedDayForm = props => {
  return (
    <div>
      <h3><b>New Worked Day</b></h3>
      <FormikWorkedDay onSubmit={props.createWorkedDay} />
    </div>
  );
};

const mapDispatchToProps = (dispatch, ownProps) => ({
  createWorkedDay: values =>
    dispatch(
      workedDayActions.create(
        ownProps.projectId,
        ownProps.monthPaymentId,
        values
      )
    )
});

export default connect(
  null,
  mapDispatchToProps
)(CreateWorkedDayForm);
