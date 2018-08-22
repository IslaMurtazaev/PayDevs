import React from "react";
import { withFormik, Form, Field } from "formik";

const HourPaymentInput = ({ errors, touched }) => {
  return (
    <Form className="rate-form">
      <div>{touched.rate && errors.rate && <p>{errors.rate}</p>}</div>
      <label> New rate: </label>
      <div />
      <Field
        name="rate"
        type="number"
        className="form-control"
        placeholder={"rate..."}
      />
      <div />
      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikHourPayment = withFormik({
  mapPropsToValues({ id, projectId, rate }) {
    return {
      rate: rate || 0,
      projectId: projectId,
      id: id
    };
  },
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    resetForm();
  }
})(HourPaymentInput);

export default FormikHourPayment;
