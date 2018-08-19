import React, { Component } from "react";
import { connect } from "react-redux";

import {tasklyActions} from '../actions/taskly';
import TaskItem from './TaskItem'



class Tasks extends Component {
  onClick() {
    this.props.onGetAllProjects();
  }

  componentDidMount() {
    const { project } = this.props;
    this.props.onGetAllTasks(project.id);
  }

  render() {
    const tasks = this.props.tasks
    const { project } = this.props;
    console.log(project)

    return (
      <div>
        <ul>
          {tasks.map(task=>
            <li key={task.id}>
                <TaskItem task={task} onDelete={this.props.onDeleteTasks} projectId={project.id}/>
            </li>

          )}
        </ul>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
    // let project = state.projects.find(
    //   product => product.id === Number(ownProps.match.params.id)
    // );
    
    return {
      tasks: state.tasks
    };
  };

const mapDispatchToProps = (dispatch) => {
    return {
        onGetAllTasks: (projectId) => {
            dispatch(tasklyActions.getAll(projectId))
        },
        onDeleteTasks: (taskId) => {
            dispatch(tasklyActions.taksDelete(taskId))
        }
    }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Tasks);
