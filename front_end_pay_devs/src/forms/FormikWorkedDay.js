import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const WorkedDayInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <label>Date: </label>
      <div>
        {touched.day && errors.day && <p>{errors.day}</p>}
      </div>
      <div>
        <DateTimePicker
          name="day"
          type="date"
          value={values.day}
          onChange={value => setFieldValue("day", value)}
        />
      </div>

      <label>
        Date2:
        <Field name="day" type="date" />
      </label>

      <label>
        Paid:
        <Field name="paid" type="checkbox" checked={values.paid} />
      </label>

      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikProject = withFormik({
  mapPropsToValues({
    id,
    day,
    paid
  }) {
    return {
      id: id || null,
      day: (day && new Date(day)) || new Date(),
      paid: (paid === false ? false : true )
    };
  },
  validationSchema: Yup.object().shape({
    day: Yup.date().required("Date is required"),
  }),
  handleSubmit(values, { props }) {
    props.onSubmit(values);
  }
})(WorkedDayInput);

export default FormikWorkedDay;
