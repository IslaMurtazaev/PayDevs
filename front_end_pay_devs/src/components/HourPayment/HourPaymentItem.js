import React, { Component } from "react";
import {Link} from "react-router-dom";

class HourPaymnetItem extends Component {

    onClickDelete(hourPaymnetId){
        this.props.onDelete(hourPaymnetId);

    }

    render() {
        const { hourPaymnet, projectId } = this.props;

        return (
            <div>
                <div>Rate: {hourPaymnet.rate}</div>
                <button><Link to={`/project/${projectId}/Taskly/${hourPaymnet.id}/update`}>UPDATE</Link></button>
                <button onClick={this.onClickDelete.bind(this, hourPaymnet.id)}>DELETE</button>
            </div>
        );
    }
}

export default HourPaymnetItem;