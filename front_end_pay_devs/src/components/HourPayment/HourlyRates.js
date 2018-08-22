import React, { Component } from "react";
import { connect } from "react-redux";

import { hourPaymentActions } from "../../actions/hourPayment";
import HourlyRate from "./HourlyRate";
import CreateHourPayment from "./CreateHourPayment";

class HourPayments extends Component {
  componentDidMount() {
    this.props.getAllHourPayments(this.props.projectId);
  }

  render() {
    const { hourPayments, projectId, removeHourPayment } = this.props;

    return (
      <div>
        { hourPayments.length > 0 && <h3 className="rateHeader">Select one of your current rates:</h3> }
        <div>
          {hourPayments.map(hourPayment => (
            <HourlyRate
              key={hourPayment.id}
              projectId={projectId}
              hourPayment={hourPayment}
              onRemove={removeHourPayment}
            />
          ))}
        </div>

        <CreateHourPayment projectId={projectId} />
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
