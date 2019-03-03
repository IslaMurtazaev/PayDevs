import React, { Component } from "react";

import TaskItem from "./TaskItem";
import CreateTask from "./CreateTask";

class Tasks extends Component {
  componentWillMount() {
    let { tasks, projectId, getAllTasks } = this.props;
    if (!tasks.length || tasks[0].projectId !== projectId)
      getAllTasks(projectId);
  }

  render() {
    const { tasks, projectId, removeTask } = this.props;

    return (
      <div>
        {tasks.length > 0 && <h3 className="header">Your tasks</h3>}

        <div className="tasks">
          {tasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onDelete={removeTask}
              projectId={projectId}
            />
          ))}
        </div>

        <CreateTask projectId={projectId} />
      </div>
    );
  }
}

export default Tasks;
