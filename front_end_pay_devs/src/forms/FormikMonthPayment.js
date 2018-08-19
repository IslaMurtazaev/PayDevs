import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const MonthPaymentInput = ({ errors, touched }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <div>
        {touched.rate && errors.rate && <p>error.rate</p>}
        <label>
          Rate:
          <Field
            name="rate"
            type="number"
            className="form-control"
            placeholder={"rate..."}
          />
        </label>
      </div>

      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikMonthPayment = withFormik({
  mapPropsToValues({ id, rate, projectId }) {
    return {
      // id: id || null,
      rate: rate || 0,
      projectId: projectId || null
    };
  },
  validationSchema: Yup.object().shape({
    rate: Yup.number().required("Rate is required")
  }),
  handleSubmit(values, { props }) {
    props.onSubmit(values.projectId, values);
  }
})(MonthPaymentInput);

export default FormikMonthPayment;
