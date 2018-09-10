import { connect } from "react-redux";

import workedDayActions from "../../actions/workedDay";
import WorkedDaysScreen from "./WorkedDaysScreen";

const mapStateToProps = state => {
  return {
    workedDays: state.workedDays
  };
};

const mapDispatchersToProps = (dispatch, ownProps) => ({
  getAllWorkedDays: () =>
    dispatch(workedDayActions.getAll(+ownProps.match.params.monthPaymentId)),
  removeWorkedDay: workedDayId => dispatch(workedDayActions.remove(workedDayId))
});

export default connect(
  mapStateToProps,
  mapDispatchersToProps
)(WorkedDaysScreen);
