import React, { Component } from "react";
import { withFormik, Form, Field } from "formik";
import * as Yup from "yup";

class TasklyInput extends Component {
  render() {
    let { values } = this.props;

    return (
      <Form className="task-form">
        <label>Title: </label>
        {this.checkValidation("title")}
        <Field
          name="title"
          type="text"
          className="titleInput form-control"
          placeholder="title..."
        />
        <div />

        <label>Description: </label>
        <div />
        <Field
          name="description"
          type="text"
          className="descriptionInput form-control"
          placeholder={"description..."}
        />
        <div />

        <label>Price: </label>
        {this.checkValidation("price")}
        <div />
        <Field
          name="price"
          type="number"
          className="priceInput form-control"
          placeholder={"price..."}
        />
        <div />

        <label>
          Paid:{" "}
          <Field
            name="paid"
            type="checkbox"
            className="paidCheckbox"
            checked={values.paid}
          />
        </label>
        <div />
        
        <label>
          Completed:{" "}
          <Field
            name="completed"
            type="checkbox"
            className="completedCheckbox"
            checked={values.completed}
          />
        </label>
        <div />
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
      price: price || "",
      paid: paid || false,
      completed: completed || false,
      projectId: projectId,
      id: id
    };
  },
  validationSchema: Yup.object().shape({
    title: Yup.string().required("Title is required"),
    price: Yup.number()
      .positive()
      .required("Price is required")
  }),
  handleSubmit(values, { props, resetForm }) {
    props.onSubmit(values);
    if (!values.id) resetForm();
  }
})(TasklyInput);

export default FormikTaskly;
