import React, { Component } from "react";
import { Link } from "react-router-dom";


class TaskItem extends Component {
  onClickDelete(taskId) {
    this.props.onDelete(taskId);
  }

  render() {
    const { task, projectId } = this.props;

    return (
      <div className="tasks">
        <h4 className="taskTitle"><b>Title:</b> {task.title}</h4>
        <h4 className="taskDescription"><b>Description:</b> {task.description}</h4>
        <h4 className="taskPrice"><b>Price:</b> {task.price}</h4>
        <h4 className="taskPaid">{task.paid ? "" : "not"} <b>paid</b></h4>
        <h4 className="taskCompleted"><b>{task.completed ? "Completed" : "Uncompleted"}</b></h4>
        <Link className="reactLink" to={`/project/${projectId}/Taskly/${task.id}/update`}>
          <button className="updateButton btn btn-warning" type="button">
            Update
          </button>
        </Link>
        <button type="button" className="btn btn-danger"
         onClick={this.onClickDelete.bind(this, task.id)}>Delete</button>
        </div>
    );
  }
}

export default TaskItem;
