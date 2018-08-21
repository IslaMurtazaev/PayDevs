import React, { Component } from "react";
import { connect } from "react-redux";
import FormikHourPayment from "../../forms/FormikHourPayment";
import { hourPaymentActions } from "../../actions/hourPayment";
import { Redirect } from "react-router-dom";

class CreateHourPayment extends Component {
  render() {
    let project = this.props.project;
    if (!Object.keys(project).length)
      return <Redirect from="/project/:id" to="/" />;

    return (
      <div>
        <h4>Create a new hour rate</h4>
        <FormikHourPayment
          projectId={project.id}
          onSubmit={this.props.createHourPayment}
        />
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  let project = state.projects.find(
    project => project.id === ownProps.projectId
  );
  return {
    hourPayment: state.hourPayment,
    project
  };
};

const mapDispatchToProps = dispatch => {
  return {
    createHourPayment: values => dispatch(hourPaymentActions.create(values))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(CreateHourPayment);
