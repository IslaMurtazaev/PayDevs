import React from "react";
import { withFormik, Form, Field } from "formik";


const HourPaymentInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <label>Title: </label>
      <div>{touched.title && errors.title && <p>{errors.title}</p>}</div>
      <label>Rate:  </label>
      <div></div>
      <Field
        name="rate"
        type="number"
        className="form-control"
        placeholder={"rate..."}
      />
      <div></div>
      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikHourPayment = withFormik({
  mapPropsToValues({
    id,
    projectId,
    rate,
  }) {
    return {
      rate: rate || 0,
      projectId: projectId,
      id: id,


    };
  },
  handleSubmit(values, { props }) {

    props.onSubmit(values);
  }
})(HourPaymentInput);

export default FormikHourPayment;
