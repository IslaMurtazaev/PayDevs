import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const WorkedDayInput = ({ values, errors, touched }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <div>{touched.day && errors.day && <p>{errors.day}</p>}</div>

      <div>
        <label>
          Date:
          <Field className="form-control" name="day" type="date" />
        </label>
      </div>

      <label>
        Paid:
        <Field
          className="form-control"
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
};

const FormikWorkedDay = withFormik({
  mapPropsToValues({ id, day, paid }) {
    return {
      id: id || null,
      day: (day && new Date(day)) || new Date(),
      paid: paid === true ? true : false
    };
  },
  validationSchema: Yup.object().shape({
    day: Yup.date().required("Date is required")
  }),
  handleSubmit(values, { props }) {
    props.onSubmit(values);
  }
})(WorkedDayInput);

export default FormikWorkedDay;
