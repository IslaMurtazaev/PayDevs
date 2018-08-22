import React from "react";
import { connect } from "react-redux";

import FormikMonthPayment from "../../forms/FormikMonthPayment";
import monthPaymentActions from "../../actions/monthPayment";

const CreateMonthPaymentForm = props => {
  return (
    <div>
      <FormikMonthPayment projectId={props.projectId} onSubmit={(projectId, values) => props.createMonthPayment(projectId, values)} />
    </div>
  );
};

const mapDispatchToProps = dispatch => {
  return {
    createMonthPayment: (projectId, values) =>
      dispatch(monthPaymentActions.create(projectId, values))
  };
};

export default connect(
  null,
  mapDispatchToProps
)(CreateMonthPaymentForm);
