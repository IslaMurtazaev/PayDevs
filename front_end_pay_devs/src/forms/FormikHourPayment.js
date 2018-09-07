import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const HourPaymentInput = ({ errors, touched }) => {
  return (
    <Form className="rate-form">
      <label>New rate: </label>
      <div className="validation-error">{touched.rate && errors.rate && <p>{errors.rate}</p>}</div>
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
};

const FormikHourPayment = withFormik({
  mapPropsToValues({ projectId, rate }) {
    return {
      rate: rate || 0,
      projectId: projectId
    };
  },
  validationSchema: Yup.object().shape({
    rate: Yup.number().positive().required("Rate is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    resetForm();
  }
})(HourPaymentInput);

export default FormikHourPayment;
