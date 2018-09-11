import React, { Component } from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

class HourPaymentInput extends Component {
  render() {
    return (
      <Form className="rate-form">
        <label>New rate: </label>
        {this.checkValidation("rate")}
        <Field
          name="rate"
          type="number"
          className="form-control rateHourPaymnet"
          placeholder={"rate..."}
        />
        <button
          className="btn btn-primary form-control newRateHourPayment"
          type="submit"
        >
          submit
        </button>
      </Form>
    );
  }

  checkValidation(attr) {
    const { errors, touched } = this.props;

    return (
      <div className="validation-error">
        {touched[attr] && errors[attr] && <p>{errors[attr]}</p>}
      </div>
    );
  }
}

const FormikHourPayment = withFormik({
  mapPropsToValues({ projectId, rate }) {
    return {
      rate: rate || 0,
      projectId: projectId
    };
  },
  validationSchema: Yup.object().shape({
    rate: Yup.number()
      .positive()
      .required("Rate is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    resetForm();
  }
})(HourPaymentInput);

export default FormikHourPayment;
