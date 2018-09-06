import React from "react";
import { withFormik, Form, Field } from "formik";
import DateTimePicker from "react-datetime-picker";

const WorkInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="worked-time-form" >
      <label>Start-work: </label>
      <div>
        {touched.start_date && errors.start_date && <p>{errors.start_date}</p>}
      </div>
      <div>
        <DateTimePicker
          name="start_work"
          type="datetime"
          value={values.start_work}
          onChange={value => setFieldValue("start_work", value)}
        />
      </div>

      <label>End-work: </label>
      <div>
        {touched.end_date && errors.end_date && <p>{errors.end_date}</p>}
      </div>
      <div>
        <DateTimePicker
          name="end_work"
          type="datetime"
          value={values.end_work}
          onChange={value => setFieldValue("end_work", value)}
        />
      </div>
      <label>
        Paid:
        <Field name="paid" type="checkbox" checked={values.paid} className="workTimePaid"/>
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
    projectId,
    hourPaymentId,
    start_work,
    end_work,
    paid
  }) {
    return {
      id: id || null,
      start_work: (start_work && new Date(start_work)) || new Date(),
      end_work: (end_work && new Date(end_work)) || new Date(),
      projectId: projectId,
      hourPaymentId: hourPaymentId,
      paid: paid
    };
  },
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(WorkInput);

export default FormikProject;
