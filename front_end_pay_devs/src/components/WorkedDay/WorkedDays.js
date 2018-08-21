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
        {this.props.workedDays.length > 0 && <h3>Your Worked Days</h3>}
        <div>
          {this.props.workedDays.map(workedDay => (
            <WorkedDay
              key={workedDay.id}
              workedDay={workedDay}
              projectId={+this.props.match.params.id}
              monthPaymentId={+this.props.match.params.monthPaymentId}
            />
          ))}
        </div>

        <hr />

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
