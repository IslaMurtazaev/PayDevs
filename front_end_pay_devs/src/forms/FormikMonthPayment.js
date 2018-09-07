import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const MonthPaymentInput = ({ errors, touched }) => {
  return (
    <Form className="rate-form">
      <label>
      <div className="validation-error">
        {touched.rate && errors.rate && <p>error.rate</p>}
      </div>
        New rate:
        <Field
          name="rate"
          type="number"
          className="form-control rateMonthPaymnet"
          placeholder={"rate..."}
        />
      </label>

      <button
        className="btn btn-primary form-control newRateMonthPayment"
        type="submit"
      >
        submit
      </button>
    </Form>
  );
};

const FormikMonthPayment = withFormik({
  mapPropsToValues({ rate, projectId }) {
    return {
      rate: rate || 0,
      projectId: projectId || null
    };
  },
  validationSchema: Yup.object().shape({
    rate: Yup.number().positive().required("Rate is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values.projectId, values);
    resetForm();
  }
})(MonthPaymentInput);

export default FormikMonthPayment;
