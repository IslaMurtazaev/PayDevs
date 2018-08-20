import React, {Component} from 'react';
import { connect } from "react-redux";
import FormikHourPayment from "../../forms/FormikHourPayment";
import FormikWorkTime from "../../forms/FormikWorkTime";
import { hourPaymentActions} from "../../actions/hourPayment";
import {workTimeActions } from "../../actions/workTime"


class CreateHourPayment extends Component {

  render(){
      let project = this.props.project;
      let hourPayment = this.props.hourPayment;
      console.log(hourPayment)
      
      return (
          <div>
          <h1>Create a new Project</h1>
         <FormikHourPayment 
          projectId={project.id}
          onSubmit={this.props.createHourPayment} 
          />
          {/* {Object.keys(hourPayment).length && <FormikWorkTime onSubmit={this.props.createWorkTime} 
          projectId={project.id} 
          hourPaymentId = {this.props.hourPayment.id}
          /> */}
        }
          </div>
      );
    }
};

const mapStateToProps = (state, ownProps) => {

    let project = state.projects.find(
      project => project.id === Number(ownProps.match.params.id)
    );
    return {
      hourPayment: state.hourPayment,
      workTimes: state.workTimes.find(workTime => workTime.hour_payment_id === state.hourPayment.id),
      project,
    };
  };

const mapDispatchToProps = dispatch => {
  return {
    createHourPayment: values => dispatch(hourPaymentActions.create(values)),
    createWorkTime: values => {
      dispatch(workTimeActions.create(values))
    },
    onGetAll: (projectId, hourPaymentId) => dispatch(workTimeActions.getAll(projectId, hourPaymentId))
  };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(CreateHourPayment);
