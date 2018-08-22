import React from "react";
import { connect } from "react-redux";

import FormikWorkedDay from "../../forms/FormikWorkedDay";
import workedDayActions from "../../actions/workedDay";

const CreateWorkedDayForm = props => {
  return (
    <div>
<<<<<<< HEAD
      <h3><b>New Worked Day</b></h3>
=======
      <h4>Create Worked Day</h4>
>>>>>>> 3f3c0041ff453f04a3f7cc836bf62aaa25342d9d
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
