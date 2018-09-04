import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

const TasklyInput = ({ values, errors, touched, setValues }) => {
  return (
    <Form className="task-form">
      <label>Title: </label>
      <div>{touched.title && errors.title && <p>{errors.title}</p>}</div>
      <Field
        name="title"
        type="text"
        className="form-control"
        placeholder="title..."
      />
      <div />
      <label>Description: </label>
      <div />
      <Field
        name="description"
        type="text"
        className="form-control"
        placeholder={"description..."}
      />
      <div />
      <label>Price: </label>
      <div />
      <Field
        name="price"
        type="number"
        className="form-control"
        placeholder={"price..."}
      />

      <div />
      <label>
        {" "}
        Paid:
        <Field name="paid" type="checkbox" checked={values.paid} />
      </label>
      <div />
      <label>
        Completed:
        <Field name="completed" type="checkbox" checked={values.completed} />
      </label>
      <div />
      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikTaskly = withFormik({
  mapPropsToValues({
    id,
    projectId,
    title,
    description,
    price,
    paid,
    completed
  }) {
    return {
      title: title || "",
      description: description || "",
      price: price || 0,
      paid: paid || false,
      completed: completed || false,
      projectId: projectId,
      id: id
    };
  },
  validationSchema: Yup.object().shape({
    title: Yup.string().required("Title is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(TasklyInput);

export default FormikTaskly;
