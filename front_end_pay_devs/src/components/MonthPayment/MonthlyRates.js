import React, { Component } from "react";
import { connect } from "react-redux";

import monthPaymentActions from "../../actions/monthPayment";
import MonthRate from "./MonthlyRate";
import CreateMonthPaymentForm from "./CreateMonthPaymentForm";

class MonthRates extends Component {
  componentDidMount() {
    this.props.getAllMonthPayments(this.props.projectId);
  }

  render() {
    return (
      <div>
        {this.props.monthPayments.length > 0 && <h3 className="rateHeader">Select one of your current rates:</h3>}
        <div>
          {this.props.monthPayments.map(monthPayment => (
            <MonthRate
              key={monthPayment.id}
              monthPayment={monthPayment}
              projectId={this.props.projectId}
              onRemove={monthPaymentId =>
                this.props.removeMonthPayment(monthPaymentId)
              }
            />
          ))}
        </div>

        <hr />

        <CreateMonthPaymentForm projectId={this.props.projectId}  />
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
