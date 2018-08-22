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
        <h4><b>Title:</b>{task.title}</h4>
        <h4><b>Description:</b> {task.description}</h4>
        <h4><b>Price:</b> {task.price}</h4>
        <button type="button">
          <Link className="updateButton" to={`/project/${projectId}/Taskly/${task.id}/update`}>
            Update
          </Link>
        </button>
        <button type="button"  
         onClick={this.onClickDelete.bind(this, task.id)}>Delete</button>
        </div>
    );
  }
}

export default TaskItem;
