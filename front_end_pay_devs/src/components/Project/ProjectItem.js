import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../../actions/project";
import { Link } from "react-router-dom";
import Tasks from "../../components/Task/Tasks";
import HourPayments from "../../components/HourPayment/HourlyRates";
import MonthRates from "../MonthPayment/MonthlyRates";

class ProjectItem extends Component {
  componentDidMount() {
    if (!this.props.project.title) this.props.getProject();
  }

  render() {
    let { project, getTotal, removeProject } = this.props;

    let sessionsType;
    let type_of_payment;
    switch (project.type_of_payment) {
      case "M_P":
        type_of_payment = "Monthly";
        sessionsType = <MonthRates projectId={project.id} />;
        break;
      case "H_P":
        type_of_payment = "Hourly";
        sessionsType = <HourPayments projectId={project.id} />;
        break;
      case "T_P":
        type_of_payment = "Taskly";
        sessionsType = <Tasks projectId={project.id} />;
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
            onClick={() => getTotal(project.id)}
          >
            Total
          </button>

          <Link to={`${project.id}/update`}>
            <button type="button" className="btn btn-warning btn-lg">
              Update project
            </button>
          </Link>

          <button
            type="button"
            className="removeProject btn btn-danger btn-lg"
            onClick={() => removeProject(project.id)}
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
