import React, {Component} from 'react';
import { connect } from "react-redux";
import FormikHourPayment from "../../forms/FormikHourPayment";
// import FormikWorkTime from "../../forms/FormikWorkTime";
import { hourPaymentActions} from "../../actions/hourPayment";
import {Link, Redirect} from "react-router-dom";


class CreateHourPayment extends Component {

  render(){
      let project = this.props.project;
      if (!Object.keys(project).length)
      return <Redirect from="/project/:id" to="/" />;
      
      
      return (
          <div>
          <h1>Create a new Project</h1>
         <FormikHourPayment 
          projectId={project.id}
          onSubmit={this.props.createHourPayment} 
          />
          <Link to="">Create Work Time</Link>
            
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
      // workTimes: state.workTimes.find(workTime => workTime.hour_payment_id === state.hourPayment.id),
      project,
    };
  };

const mapDispatchToProps = dispatch => {
  return {
    createHourPayment: values => dispatch(hourPaymentActions.create(values)),
    
    
  };
};

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(CreateHourPayment);
