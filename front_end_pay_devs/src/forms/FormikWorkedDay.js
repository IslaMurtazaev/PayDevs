import React, { Component } from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

class WorkedDayInput extends Component {
  render() {
    let { values } = this.props;

    return (
      <Form className="worked-day-form">
        <div>
          <label>
            Date:
            {this.checkValidation("day")}
            <Field className="form-control dayWokedDay" name="day" type="date" />
          </label>
        </div>
  
        <label>
          Paid:
          <Field
            className="form-control workDayPaid"
            name="paid"
            type="checkbox"
            checked={values.paid}
          />
        </label>
  
        <button className="btn btn-primary form-control" type="submit">
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
};

const FormikWorkedDay = withFormik({
  mapPropsToValues({ id, day, paid }) {
    return {
      id: id || null,
      day: day || "",
      paid: paid === true ? true : false
    };
  },
  validationSchema: Yup.object().shape({
    day: Yup.date().required("Date is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(WorkedDayInput);

export default FormikWorkedDay;
