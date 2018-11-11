import React, { Component } from "react";

import WorkedDay from "./WorkedDay";
import CreateWorkedDayForm from "./CreateWorkedDayForm";

class WorkedDays extends Component {
  componentWillMount() {
    let { workedDays, getAllWorkedDays } = this.props;
    let monthPaymentId = this.props.match.params.monthPaymentId;

    if (!workedDays.length || workedDays[0].monthPaymentId !== monthPaymentId)
      getAllWorkedDays();
  }

  render() {
    return (
      <div>
        {this.props.workedDays.length > 0 && (
          <h3 className="header">
            <b>Your Worked Days</b>
          </h3>
        )}
        <div>
          {this.props.workedDays.map(workedDay => (
            <WorkedDay
              key={workedDay.id}
              workedDay={workedDay}
              projectId={+this.props.match.params.id}
              monthPaymentId={+this.props.match.params.monthPaymentId}
              onRemove={this.props.removeWorkedDay}
            />
          ))}
        </div>

        <CreateWorkedDayForm
          projectId={+this.props.match.params.id}
          monthPaymentId={+this.props.match.params.monthPaymentId}
        />
      </div>
    );
  }
}

export default WorkedDays;
