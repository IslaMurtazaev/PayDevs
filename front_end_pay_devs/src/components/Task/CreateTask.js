import React from "react";
import FormikTaskly from "../../forms/FormikTask";
import { tasklyActions } from "../../actions/task";
import { connect } from "react-redux";

const CreateTaskForm = props => {
  return (
    <div>
      <h3 className="taskHeader"> Create a new Task</h3>
      <FormikTaskly onSubmit={props.createTaskly} />
    </div>
  );
};

const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    createTaskly: values =>
      dispatch(tasklyActions.create(values, ownProps.projectId))
  };
};

const mapStateToProps = (state, ownProps) => {
  let project = state.projects.find(
    project => project.id === ownProps.projectId
  );
  return {
    project: project ? project : state.project
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CreateTaskForm);
