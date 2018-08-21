import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";
import DateTimePicker from "react-datetime-picker";
// import "../App.css";

const ProjectInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <div>
    <Form >
      <label>Title: </label>
      <div>{touched.title && errors.title && <p>{errors.title}</p>}</div>
      <Field
        name="title"
        type="text"
        className="form-control"
        placeholder="title..."
      />

      <label>Description: </label>
      <Field
        name="description"
        type="textarea"
        className="description"
        placeholder="description..."
      />

      <label>Start-date: </label>
      <div>
        {touched.start_date && errors.start_date && <p>{errors.start_date}</p>}
      </div>
      <div>
        <DateTimePicker
          name="start_date"
          type="datetime"
          className="dateTime"
          value={values.start_date}
          onChange={value => setFieldValue("start_date", value)}
        />
      </div>

      <label>End-date: </label>
      <div>
        {touched.end_date && errors.end_date && <p>{errors.end_date}</p>}
      </div>
      <div>
        <DateTimePicker
          name="end_date"
          type="datetime"
          value={values.end_date}
          onChange={value => setFieldValue("end_date", value)}
        />
      </div>

      <label>Type of payment: </label>
      <Field component="select" name="type_of_payment" className="form-control">
        <option value="M_P">Monthly</option>
        <option value="H_P">Hourly</option>
        <option value="T_P">Taskly</option>
      </Field>

      <label>
        Active:
        <Field name="status" type="checkbox" checked={values.status} />
      </label>
    </Form>
    <br/>
    <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </div>
  );
};

const FormikProject = withFormik({
  mapPropsToValues({
    id,
    title,
    description,
    start_date,
    end_date,
    type_of_payment,
    status
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
