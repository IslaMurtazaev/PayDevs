import React, { Component } from "react";
import { connect } from "react-redux";
import {workTimeActions} from '../../actions/workTime';
import WorkTimeItem from "./WorkTimeItem"
import FormikWorkTime from "../../forms/FormikWorkTime";




class WorkTimes extends Component {
  onClick() {
    this.props.onGetAllProjects();
  }

  componentDidMount() {
    const {hourPayment } = this.props;
    this.props.onGetAll(hourPayment.id);
  }

  render() {
    
    const { hourPayment, projectId, workTimes} = this.props;
    return (
      <div>
        <ul>
          {workTimes.map(workTime=>(
            <li key={workTime.id}>
                <WorkTimeItem hourPayment={hourPayment}  
                workTime = {workTime}
                projectId={projectId} 
                onDelete={this.props.onDeletehourPayment}/>
            </li>)
          )
        }
        </ul>
        <FormikWorkTime onSubmit={this.props.createWorkTime} 
          projectId={projectId} 
          hourPaymentId = {this.props.hourPayment.id}
          /> 
          
      </div>
    );
  }
}

const mapStateToProps = (state) => {
    
    return {
      workTimes: state.workTimes
    };
  };

const mapDispatchToProps = (dispatch) => {
    return {
        onGetAll:  hourPaymentId => dispatch(workTimeActions.getAll(hourPaymentId)),
        onDeletehourPayment: (hourId) => {
            dispatch(workTimeActions.deleteWork(hourId))
        },
        createWorkTime: values => {
            dispatch(workTimeActions.create(values))
          },
    }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(WorkTimes);
