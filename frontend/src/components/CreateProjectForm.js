import React from 'react';
import FormikProject from "../forms/FormikProject";
import { projectActions } from "../actions/project";
import { connect } from "react-redux";

const CreateProjectForm = props => {
  return (
    <div>
      <h1>Create a new Project</h1>
      <FormikProject onSubmit={props.createProject} />
    </div>
  );
};

const mapDispatchToProps = dispatch => {
  return {
    createProject: values => dispatch(projectActions.create(values))
  };
};

export default connect(
  null,
  mapDispatchToProps
)(CreateProjectForm);
