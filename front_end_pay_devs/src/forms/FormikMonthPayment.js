import React, { Component } from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

class MonthPaymentInput extends Component {
  render() {
    return (
      <Form className="rate-form">
        <label>
          {this.checkValidation("rate")}
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

const FormikMonthPayment = withFormik({
  mapPropsToValues({ rate, projectId }) {
    return {
      rate: rate || 0,
      projectId: projectId || null
    };
  },
  validationSchema: Yup.object().shape({
    rate: Yup.number()
      .positive()
      .required("Rate is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values.projectId, values);
    resetForm();
  }
})(MonthPaymentInput);

export default FormikMonthPayment;
