import React, { Component } from "react";
import { connect } from "react-redux";

import workTimeActions from "../../actions/workTime";
import WorkTime from "./WorkTime";
import FormikWorkTime from "../../forms/FormikWorkTime";

class WorkTimes extends Component {
  componentDidMount() {
    this.props.getAllWorkTimes(this.props.match.params.hourPaymentId);
  }

  render() {
    const { workTimes } = this.props;

    return (
      <div>
        {workTimes.length > 0 && <h3>Your Worked Hours</h3>}
        <div>
          {workTimes.map(workTime => (
            <WorkTime
              key={workTime.id}
              workTime={workTime}
              projectId={+this.props.match.params.id}
              hourPaymentId={+this.props.match.params.hourPaymentId}
              onRemove={this.props.removeWorkTime}
            />
          ))}
        </div>

        <hr />

        <h4>Create a new Work Time</h4>
        <FormikWorkTime
          onSubmit={this.props.createWorkTime}
          projectId={+this.props.match.params.id}
          hourPaymentId={+this.props.match.params.hourPaymentId}
        />
      </div>
    );
  }
}

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
)(WorkTimes);
