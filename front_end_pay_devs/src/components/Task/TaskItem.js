import React, { Component } from "react";
import {Link} from "react-router-dom";

class TaskItem extends Component {

    onClickDelete(taskId){
        this.props.onDelete(taskId);

    }

    render() {
        const { task, projectId } = this.props;

        return (
            <div>
                <h4>{task.title}</h4>
                <div>Description: {task.description}</div>
                <div>Price: {task.price}</div>
                <button><Link to={`/project/${projectId}/Taskly/${task.id}/update`}>UPDATE</Link></button>
                <button onClick={this.onClickDelete.bind(this, task.id)}>DELETE</button>
            </div>
        );
    }
}

export default TaskItem;