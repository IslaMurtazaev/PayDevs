import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";
import DateTimePicker from "react-datetime-picker";

const WorkInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="worked-time-form" >
      <label>Start-work: </label>
      <div className="validation-error">
        {touched.start_work && errors.start_work && <p>{errors.start_work}</p>}
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
      <div className="validation-error">
        {touched.end_work && errors.end_work && <p>{errors.end_work}</p>}
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
  validationSchema: Yup.object().shape({
    start_work: Yup.date("Invalid date"),
    end_work: Yup.date("Invalid date")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(WorkInput);

export default FormikProject;
