import React from 'react';
import FormikTaskly from "../forms/FormikTaskly";
import { tasklyActions } from "../actions/taskly";
import { connect } from "react-redux";

const CreateTasklyForm = (props) => {
    
    return (
      <div>
        <h1>Create a new Project</h1>
        <FormikTaskly onSubmit={props.createTaskly} />
      </div>
    );
}


const mapDispatchToProps = (dispatch, ownProps) => {
    
  return {
    createTaskly: (values)=> dispatch(tasklyActions.create(values, Number(ownProps.match.params.id)))
  };
};

const mapStateToProps = (state, ownProps) => {
    let project = state.projects.find(
      product => product.id === Number(ownProps.match.params.id)
    );
    return {
      project: project ? project : state.project
    };
  };

export default connect(
    mapStateToProps,
  mapDispatchToProps
)(CreateTasklyForm);