import { connect } from "react-redux";

import workTimeActions from "../../actions/workTime";
import WorkTimesScreen from "./WorkTimesScreen";

const mapStateToProps = state => {
  return {
    workTimes: state.workTimes
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getAllWorkTimes: hourPaymentId =>
      dispatch(workTimeActions.getAll(hourPaymentId)),
    removeWorkTime: workTimeId => {
      dispatch(workTimeActions.remove(workTimeId));
    },
    createWorkTime: values => {
      dispatch(workTimeActions.create(values));
    }
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(WorkTimesScreen);
