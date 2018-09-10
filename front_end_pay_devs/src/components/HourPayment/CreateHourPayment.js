import React from "react";
import { connect } from "react-redux";
import FormikHourPayment from "../../forms/FormikHourPayment";
import { hourPaymentActions } from "../../actions/hourPayment";

const CreateHourPayment = props => {
  return (
    <FormikHourPayment
      projectId={props.projectId}
      onSubmit={props.createHourPayment}
    />
  );
};

const mapStateToProps = state => {
  return {
    hourPayment: state.hourPayment
  };
};

const mapDispatchToProps = dispatch => {
  return {
    createHourPayment: values => dispatch(hourPaymentActions.create(values))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CreateHourPayment);
