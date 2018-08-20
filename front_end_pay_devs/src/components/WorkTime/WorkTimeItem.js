import React, { Component } from "react";
// import {Link} from "react-router-dom";

class WorkTimeItem extends Component {

    onClickDelete(workTimeId){
        this.props.onDelete(workTimeId);

    }

    render() {
        const { workTime} = this.props;
        return (
            <div>
                <div>Start Work: {workTime.start_work}</div>
                <div>End Work: {workTime.end_work}</div>
                {workTime.paid ? <div>paid</div>: <div>not paid</div>}
                {/* <button><Link to={`/project/${projectId}/Hourly/${workTime.id}/update`}>UPDATE</Link></button> */}
                <button onClick={this.onClickDelete.bind(this, workTime.id)}>DELETE</button>
            </div>
        );
    }
}

export default WorkTimeItem;