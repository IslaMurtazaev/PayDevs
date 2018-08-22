import React, { Component } from "react";
import { connect } from "react-redux";

import workedDayActions from "../../actions/workedDay";
import WorkedDay from "./WorkedDay";
import CreateWorkedDayForm from "./CreateWorkedDayForm";

class WorkedDays extends Component {
  componentDidMount() {
    this.props.getAllWorkedDays();
  }

  render() {
    return (
      <div>
        {this.props.workedDays.length > 0 && <h3><b>Your Worked Days</b></h3>}
        <div className="worked">
          {this.props.workedDays.map(workedDay => (
            <WorkedDay
              key={workedDay.id}
              workedDay={workedDay}
              projectId={+this.props.match.params.id}
              monthPaymentId={+this.props.match.params.monthPaymentId}
            />
          ))}
        </div>

        <CreateWorkedDayForm projectId={+this.props.match.params.id} monthPaymentId={+this.props.match.params.monthPaymentId} />
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    workedDays: state.workedDays
  };
};

const mapDispatchersToProps = (dispatch, ownProps) => ({
  getAllWorkedDays: () =>
    dispatch(workedDayActions.getAll(+ownProps.match.params.monthPaymentId))
});

export default connect(
  mapStateToProps,
  mapDispatchersToProps
)(WorkedDays);
