import React, { Component } from "react";
import { connect } from "react-redux";

import monthPaymentActions from "../../actions/monthPayment";
import MonthRate from "./MonthRate";

class MonthRates extends Component {
  constructor(props) {
    super(props);
    this.props.getAllMonthPayments(this.props.projectId);
  }

  render() {
    if (this.props.monthPayments.length === 0) {
      return null;
    }

    return (
      <div>
        <h3 className="monthlyHeader">Select one of your current rates:</h3>
        <div>
          {this.props.monthPayments.map(monthPayment => (
            <MonthRate
              key={monthPayment.id}
              id={monthPayment.id}
              rate={monthPayment.rate}
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
