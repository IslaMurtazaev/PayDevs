import { connect } from "react-redux";

import { hourPaymentActions } from "../actions/hourPayment";
import HourlyRates from "../components/HourlyRates";

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
)(HourlyRates);
