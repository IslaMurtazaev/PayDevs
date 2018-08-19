import React, { Component } from "react";
import { connect } from "react-redux";

import {tasklyActions} from '../../actions/taskly';




class HourPayments extends Component {
  onClick() {
    this.props.onGetAllProjects();
  }

  componentDidMount() {
    const { project } = this.props;
    this.props.onGetAllTasks(project.id);
  }

  render() {
    
    const { project } = this.props;
    console.log(project)
    

    return (
      <div>
          
        <ul>
          
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
      hoursPayments: state.hoursPayments
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
)(HourPayments);
