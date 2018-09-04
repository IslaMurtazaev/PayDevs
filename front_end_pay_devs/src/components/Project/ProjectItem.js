import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../../actions/project";
import { Link } from "react-router-dom";
import Tasks from "../../components/Task/Tasks";
import HourlyRates from "../../components/HourPayment/HourlyRates";
import MonthlyRates from "../MonthPayment/MonthlyRates";

class ProjectItem extends Component {
  componentWillMount() {
    if (this.props.project.id !== +this.props.match.params.id)
      this.props.getProject();
  }

  render() {
    let { project, getTotal, removeProject } = this.props;
    let projectId = +this.props.match.params.id;

    let sessionsType;
    let type_of_payment;
    switch (project.type_of_payment) {
      case "M_P":
        type_of_payment = "Monthly";
        sessionsType = <MonthlyRates projectId={projectId} />;
        break;
      case "H_P":
        type_of_payment = "Hourly";
        sessionsType = <HourlyRates projectId={projectId} />;
        break;
      case "T_P":
        type_of_payment = "Taskly";
        sessionsType = <Tasks projectId={projectId} />;
        break;
      default:
        break;
    }

    return (
      <div className="container">
        <h1 className="projectTitle">{project.title}</h1>
        <div className="properties">
          {project.description ? (
            <h4 className="projectDescription">
              <span className="property">Description: </span>
              {project.description}
            </h4>
          ) : null}
          {project.start_date ? (
            <h4 className="projectStartDate">
              <span className="property">Start date: </span>
              {new Date(project.start_date).toDateString()}
            </h4>
          ) : null}
          {project.end_date ? (
            <h4 className="projectEndDate">
              <span className="property">End date: </span>
              {new Date(project.end_date).toDateString()}
            </h4>
          ) : null}
          <h4 className="projectTypeOfPayment">
            <span className="property">Type of payment:</span> {type_of_payment}
          </h4>
          <h4 className="projectStatus">
            <span className="property">Status:</span>
            {project.status ? "" : "not"} active
          </h4>
        </div>

        <div className="btn-group-horizontal">
          <button
            type="button"
            className="btn btn-success btn-lg"
            onClick={() => getTotal(projectId)}
          >
            Total
          </button>

          <Link to={`${projectId}/update`}>
            <button type="button" className="updateProject btn btn-warning btn-lg">
              Update project
            </button>
          </Link>

          <button
            type="button"
            className="removeProject btn btn-danger btn-lg"
            onClick={() => removeProject(projectId)}
          >
            Delete project
          </button>
        </div>

        <div className="session">{sessionsType}</div>
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => ({
  project: state.project
    ? state.project
    : state.projects.find(project => project.id === +ownProps.match.params.id)
});

const mapDispatchToProps = (dispatch, ownProps) => ({
  removeProject: id => {
    dispatch(projectActions.remove(id));
  },
  getTotal: id => {
    dispatch(projectActions.getTotal(id));
  },
  getProject: () => {
    dispatch(projectActions.get(+ownProps.match.params.id));
  }
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ProjectItem);
