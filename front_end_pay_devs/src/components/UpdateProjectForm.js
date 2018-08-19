import React from "react";
import FormikProject from "../forms/FormikProject";
import { projectActions } from "../actions/project";
import { connect } from "react-redux";

const UpdateProjectForm = props => {
  const project = props.project;
  return (
    <div>
      <h1>Update Project</h1>
      <FormikProject
        id={project.id}
        title={project.title}
        description={project.description}
        start_date={project.start_date}
        end_date={project.end_date}
        type_of_payment={project.type_of_payment}
        status={project.status}
        onSubmit={props.updateProject}
      />
    </div>
  );
};

const mapStateToProps = (state, ownProps) => {
  let project = state.projects.find(
    project => project.id === Number(ownProps.match.params.id)
  );
  return {
    project: project ? project : state.project
  };
};

const mapDispatchToProps = dispatch => {
  return {
    updateProject: values => dispatch(projectActions.update(values))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(UpdateProjectForm);
