import React, { Component } from "react";
import { connect } from "react-redux";

import { hourPaymentActions } from "../../actions/hourPayment";
import HourlyRate from "./HourlyRate";

class HourPayments extends Component {
  componentDidMount() {
    this.props.getAllHourPayments(this.props.project.id);
  }

  render() {
    const { hourPayments, project } = this.props;

    if (hourPayments.length === 0) {
      return null;
    }

    return (
      <div>
        <h3>Select one of your current rates:</h3>
        <div>
          {hourPayments.map(hourPayment => (
            <HourlyRate
              key={hourPayment.id}
              projectId={project.id}
              hourPayment={hourPayment}
              onRemove={this.props.removeHourPayment}
            />
          ))}
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    hourPayments: state.hourPayments
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getAllHourPayments: projectId => {
      dispatch(hourPaymentActions.getAll(projectId));
    },
    removeHourPayment: hourPaymentId => {
      dispatch(hourPaymentActions.remove(hourPaymentId));
    }
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(HourPayments);
