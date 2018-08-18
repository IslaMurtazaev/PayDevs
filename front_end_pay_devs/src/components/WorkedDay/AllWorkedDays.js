import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";

import workedDayActions from "../../actions/workedDay";
import WorkedDay from "./WorkedDay";

class WorkedDays extends Component {
  constructor(props) {
    super(props);
    this.props.getAllWorkedDays();
  }

  render() {
    return (
      <div>
        <h3>Your Worked Days</h3>
        <div>
          {this.props.workedDays.map(workedDay => (
            <WorkedDay
              key={workedDay.id}
              workedDay={workedDay}
              onRemove={this.props.removeWorkedDay}
            />
          ))}
        </div>
        <Link to={`/project/${this.props.match.params.id}/Monthly/${this.props.match.params.monthPaymentId}/workedDay/create`}>Create new Worked day</Link>
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
  getAllWorkedDays: () => dispatch(workedDayActions.getAll(+ownProps.match.params.monthPaymentId)),
  removeWorkedDay: workedDayId => dispatch(workedDayActions.remove(workedDayId))
});

export default connect(
  mapStateToProps,
  mapDispatchersToProps
)(WorkedDays);
