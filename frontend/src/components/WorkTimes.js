import React, { Component } from "react";

import WorkTime from "./WorkTime";
import FormikWorkTime from "../forms/FormikWorkTime";

class WorkTimes extends Component {
  componentWillMount() {
    let { workTimes, getAllWorkTimes } = this.props;
    let hourPaymentId = +this.props.match.params.hourPaymentId;

    if (!workTimes.length || workTimes[0].hourPaymentId !== hourPaymentId)
      getAllWorkTimes(hourPaymentId);
  }

  render() {
    const { workTimes, createWorkTime, removeWorkTime } = this.props;

    return (
      <div>
        {workTimes.length > 0 && (
          <h3 className="workedHoursHeader">
            <b>Your Worked Hours</b>
          </h3>
        )}
        <div>
          {workTimes.map(workTime => (
            <WorkTime
              key={workTime.id}
              workTime={workTime}
              projectId={+this.props.match.params.id}
              hourPaymentId={+this.props.match.params.hourPaymentId}
              onRemove={removeWorkTime}
            />
          ))}
        </div>

        <h3>
          <b>Create a new Work Time</b>
        </h3>
        <FormikWorkTime
          onSubmit={createWorkTime}
          projectId={+this.props.match.params.id}
          hourPaymentId={+this.props.match.params.hourPaymentId}
        />
      </div>
    );
  }
}

export default WorkTimes;
