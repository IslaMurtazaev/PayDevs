import React, { Component } from "react";
import { connect } from "react-redux";

import { tasklyActions } from "../../actions/taskly";
import TaskItem from "./TaskItem";
import CreateTask from "./CreateTask";

class Tasks extends Component {
  componentDidMount() {
    this.props.getAllTasks(this.props.project.id);
  }

  render() {
    const { tasks, project } = this.props;

    return (
      <div>
        {tasks.length > 0 && <h3 className="taskHeader">Your tasks</h3>}

        <div>
          {tasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onDelete={this.props.removeTask}
              projectId={project.id}
            />
          ))}
        </div>


        <CreateTask projectId={project.id} />
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    tasks: state.tasks
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getAllTasks: projectId => {
      dispatch(tasklyActions.getAll(projectId));
    },
    removeTask: taskId => {
      dispatch(tasklyActions.remove(taskId));
    }
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Tasks);
