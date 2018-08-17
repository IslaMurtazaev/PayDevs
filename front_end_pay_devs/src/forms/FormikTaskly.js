import React from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";



const TasklyInput = ({ values, errors, touched, setFieldValue }) => {
  return (
    <Form className="form-group" style={{ margin: 10 }}>
      <label>Title: </label>
      <div>{touched.title && errors.title && <p>{errors.title}</p>}</div>
      <Field
        name="title"
        type="text"
        className="form-control"
        placeholder="title..."
      />
      <div></div>
      <label>Description: </label>
      <div></div>
      <Field
        name="description"
        type="text"
        className="form-control"
        placeholder={"description..."}
      />
      <div></div>
      <label>Prijece: </label>
      <div></div>
      <Field
        name="price"
        type="number"
        className="form-control"
        placeholder={"price..."}
      />
      
    <div></div>
      <label> Paid: 
        <Field name="paid" type="checkbox" checked={values.paid} />
      </label>
      <div></div>
      <label>
        Completed:
        <Field name="completed" type="checkbox" checked={values.completed} />
      </label>
      <div></div>
      <button className="btn btn-primary form-control" type="submit">
        submit
      </button>
    </Form>
  );
};

const FormikTaskly = withFormik({
  mapPropsToValues({
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
      completed: completed || false

    };
  },
  validationSchema: Yup.object().shape({
    title: Yup.string().required("Title is required"),
    
  }),
  handleSubmit(values, { props }) {

    props.onSubmit(values);
  }
})(TasklyInput);

export default FormikTaskly;
