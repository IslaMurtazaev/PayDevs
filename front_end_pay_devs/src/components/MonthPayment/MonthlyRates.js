import React, { Component } from "react";
import { connect } from "react-redux";

import monthPaymentActions from "../../actions/monthPayment";
import MonthRate from "./MonthlyRate";

class MonthRates extends Component {
  componentDidMount() {
    this.props.getAllMonthPayments(this.props.projectId);
  }

  render() {
    if (this.props.monthPayments.length === 0) {
      return null;
    }

    return (
      <div>
        <h3 className="monthlyHeader">Select one of your current rates:</h3>
        <h3>Select one of your current rates:</h3>
        <div>
          {this.props.monthPayments.map(monthPayment => (
            <MonthRate
              key={monthPayment.id}
              monthPayment={monthPayment}
              onRemove={monthPaymentId =>
                this.props.removeMonthPayment(monthPaymentId)
              }
            />
          ))}
        </div>
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
)(MonthRates);
