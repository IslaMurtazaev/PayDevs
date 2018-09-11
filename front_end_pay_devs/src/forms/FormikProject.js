import React, { Component } from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";
import DateTimePicker from "react-datetime-picker";

class ProjectInput extends Component {
  render() {
    let { values, setFieldValue } = this.props;

    return (
      <Form className="form-group">
        <label>Title: </label>
        {this.checkValidation("title")}
        <Field
          name="title"
          type="text"
          className="titleInput form-control"
          placeholder="title..."
        />

        <label>Description: </label>
        <Field
          name="description"
          type="text"
          className="descriptionInput form-control"
          placeholder="description..."
        />

        <label>Start-date: </label>
        {this.checkValidation("start_date")}
        <div>
          <DateTimePicker
            name="start_date"
            type="datetime"
            value={values.start_date}
            onChange={value => setFieldValue("start_date", value)}
          />
        </div>

        <label>End-date: </label>
        {this.checkValidation("end_date")}
        <div>
          <DateTimePicker
            name="end_date"
            type="datetime"
            value={values.end_date}
            onChange={value => setFieldValue("end_date", value)}
          />
        </div>

        <label>Type of payment: </label>
        <Field
          component="select"
          name="type_of_payment"
          className="typeOfPaymentSelect form-control"
        >
          <option value="M_P">Monthly</option>
          <option value="H_P">Hourly</option>
          <option value="T_P">Taskly</option>
        </Field>

        <label>
          Active:
          <Field
            name="status"
            type="checkbox"
            className="statusCheckbox"
            checked={values.status}
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
}

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
      status: status === false ? false : true
    };
  },
  validationSchema: Yup.object().shape({
    title: Yup.string().required("Title is required"),
    start_date: Yup.date().required("Start-date is required"),
    end_date: Yup.date().required("End-date is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(ProjectInput);

export default FormikProject;
