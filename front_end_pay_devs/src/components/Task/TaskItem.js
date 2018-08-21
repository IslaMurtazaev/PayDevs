import React, { Component } from "react";
import { Link } from "react-router-dom";

class TaskItem extends Component {
  onClickDelete(taskId) {
    this.props.onDelete(taskId);
  }

  render() {
    const { task, projectId } = this.props;

    return (
      <div>
        <h4>{task.title}</h4>
        <h4>Description: {task.description}</h4>
        <h4>Price: {task.price}</h4>
        <h4>{task.completed ? "Completed" : "Uncompleted"}</h4>
        <button>
          <Link to={`/project/${projectId}/Taskly/${task.id}/update`}>
            Update
          </Link>
        </button>
        <button onClick={this.onClickDelete.bind(this, task.id)}>Delete</button>
      </div>
    );
  }
}

export default TaskItem;
