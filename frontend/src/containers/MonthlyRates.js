import { connect } from "react-redux";

import monthPaymentActions from "../actions/monthPayment";
import MonthlyRates from "../components/MonthlyRates"

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
