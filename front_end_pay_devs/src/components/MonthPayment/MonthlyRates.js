import React, { Component } from "react";
import { connect } from "react-redux";

import monthPaymentActions from "../../actions/monthPayment";
import MonthlyRate from "./MonthlyRate";
import CreateMonthPaymentForm from "./CreateMonthPaymentForm";

class MonthlyRates extends Component {
  componentWillMount() {
    let { monthPayments, projectId, getAllMonthPayments } = this.props;
    if (!monthPayments.length || monthPayments[0].projectId !== projectId)
      getAllMonthPayments(projectId);
  }

  render() {
    const { monthPayments, projectId, removeMonthPayment } = this.props;

    return (
      <div className="monthlyRates">
        {monthPayments.length > 0 && (
          <h3 className="rateHeader">Select one of your current rates:</h3>
        )}
        <div>
          {monthPayments.map(monthPayment => (
            <MonthlyRate
              key={monthPayment.id}
              monthPayment={monthPayment}
              projectId={projectId}
              onRemove={monthPaymentId => removeMonthPayment(monthPaymentId)}
            />
          ))}
        </div>

        <CreateMonthPaymentForm projectId={projectId} />
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    monthPayments: state.monthPayments
  };
};

const mapDispatchersToProps = dispatch => ({
  getAllMonthPayments: projectId =>
    dispatch(monthPaymentActions.getAll(projectId)),
  removeMonthPayment: monthPaymentId =>
    dispatch(monthPaymentActions.remove(monthPaymentId))
});

export default connect(
  mapStateToProps,
  mapDispatchersToProps
)(MonthlyRates);
