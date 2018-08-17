import React from "react";
import { connect } from "react-redux";
import FormikTaskly from "../forms/FormikTaskly"
import {tasklyActions} from '../actions/taskly';
import { Redirect } from "react-router-dom";


const UpdateTaskForm = props => {
    const task = props.task;
    if (!Object.keys(task).length)
      return <Redirect from="/project/:id" to="/" />;
    return (
    <div>
        <h1>Update Project</h1>
        <FormikTaskly 
        id={task.id}
        projectId={task.project_id}
        title={task.title}
        description={task.description}
        price={task.price}
        paid={task.paid}
        completed={task.completed}
        onSubmit={props.onUpdateTask}
        />
    </div>
    );
};

const mapStateToProps = (state, ownProps) => {
    
    let task = state.tasks.find(
    task => task.id === Number(ownProps.match.params.taskId)
    );
    return {
        task: task ? task : state.task
    };
};

const mapDispatchToProps = dispatch => {
    return {
        onUpdateTask: values => dispatch(tasklyActions.update(values))
    };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(UpdateTaskForm);