import React from "react";
import { connect } from "react-redux";
import FormikHourPayment from "../forms/FormikHourPayment"
import {hourPaymentActions} from '../actions/hourPayment';
import { Redirect } from "react-router-dom";
import WorkTimes from "../containers/WorkTimes"


const UpdateHourlyForm = props => {
    const hourPayment = props.hourPayment;
    if (!Object.keys(hourPayment).length)
      return <Redirect from="/project/:id" to="/" />;
    return (
    <div>
        <h1>Update Hour Payment</h1>
        <FormikHourPayment 
          id={hourPayment.id}
          projectId={hourPayment.project_id}
          rate = {hourPayment.rate}
          onSubmit={props.updateHourPayment} 
          />
          <WorkTimes hourPayment={hourPayment} projectId={hourPayment.project_id}></WorkTimes>
    </div>
    );
};

const mapStateToProps = (state, ownProps) => {
    
    let hourPayment = state.hourPayments.find(
        hourPayment => hourPayment.id === Number(ownProps.match.params.hourPaymentId)
    );
    return {
        hourPayment: hourPayment ? hourPayment : state.hourPayment
    };
};

const mapDispatchToProps = dispatch => {
    return {
        updateHourPayment: values => dispatch(hourPaymentActions.update(values))
    };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(UpdateHourlyForm);