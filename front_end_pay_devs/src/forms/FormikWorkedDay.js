import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const WorkedDayInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <label>Date: </label>
      <div>
        {touched.start_date && errors.start_date && <p>{errors.start_date}</p>}
      </div>
      <div>
        <DateTimePicker
          name="start_date"
          type="date"
          value={values.day}
          onChange={value => setFieldValue("start_date", value)}
        />
      </div>

      <label>Type of payment: </label>
      <Field component="select" name="type_of_payment" className="form-control">
        <option value="M_P">Monthly</option>
        <option value="H_P">Hourly</option>
        <option value="T_P">Taskly</option>
      </Field>

      <label>
        Paid:
        <Field name="paid" type="checkbox" checked={values.status} />
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
      title: title || "",
      description: description || "",
      start_date: (start_date && new Date(start_date)) || new Date(),
      end_date: (end_date && new Date(end_date)) || new Date(),
      type_of_payment: type_of_payment || "M_P",
      status: (status === false ? false : true )
    };
  },
  validationSchema: Yup.object().shape({
    title: Yup.string().required("Title is required"),
    start_date: Yup.date().required("Start-date is required"),
    end_date: Yup.date().required("End-date is required")
  }),
  handleSubmit(values, { props }) {
    props.onSubmit(values);
  }
})(ProjectInput);

export default FormikProject;
