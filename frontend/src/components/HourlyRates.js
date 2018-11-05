import React, { Component } from "react";

import HourlyRate from "./HourlyRate";
import CreateHourPayment from "../containers/CreateHourPayment";

class HourlyRates extends Component {
  componentWillMount() {
    let { hourPayments, projectId, getAllHourPayments } = this.props;
    if (!hourPayments.length || hourPayments[0].projectId !== projectId)
      getAllHourPayments(projectId);
  }

  render() {
    const { hourPayments, projectId, removeHourPayment } = this.props;

    return (
      <div className="hourlyRates">
        {hourPayments.length > 0 && (
          <h3 className="rateHeader">Select one of your current rates:</h3>
        )}
        <div>
          {hourPayments.map(hourPayment => (
            <HourlyRate
              key={hourPayment.id}
              projectId={projectId}
              hourPayment={hourPayment}
              onRemove={removeHourPayment}
            />
          ))}
        </div>

        <CreateHourPayment projectId={projectId} />
      </div>
    );
  }
}

export default HourlyRates;
