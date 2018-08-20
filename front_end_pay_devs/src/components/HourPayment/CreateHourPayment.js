import React from 'react';
import { connect } from "react-redux";
import FormikHourPayment from "../../forms/FormikHourPayment";
import FormikWorkTime from "../../forms/FormikWorkTime";
import { hourPaymentActions} from "../../actions/hourPayment";
import {workTimeActions } from "../../actions/workTime"


const CreateHourPayment = props => {
    let project = props.project;
    let hourPayment = props.hourPayment;
    console.log(props.hourPayment)
    return (
        <div>
        <h1>Create a new Project</h1>
        <FormikHourPayment 
        projectId={project.id}
        onSubmit={props.createHourPayment} 
        />
        {Object.keys(hourPayment).length && <FormikWorkTime onSubmit={props.createWorkTime} 
        projectId={project.id} 
        hourPaymentId = {hourPayment.id}
        />
      }
        </div>
    );
};

const mapStateToProps = (state, ownProps) => {

    let project = state.projects.find(
      project => project.id === Number(ownProps.match.params.id)
    );
    return {
      hourPayment: state.hourPayment,
      project,
    };
  };

const mapDispatchToProps = dispatch => {
  return {
    createHourPayment: values => dispatch(hourPaymentActions.create(values)),
    createWorkTime: values => dispatch(workTimeActions.create(values))
  };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(CreateHourPayment);
