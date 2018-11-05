import React, { Component } from "react";
import { Link } from "react-router-dom";

import Tasks from "../containers/Tasks";
import HourlyRates from "../containers/HourlyRates";
import MonthlyRates from "../containers/MonthlyRates";

class Project extends Component {
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
            <p className="projectDescription">
              <span className="property">Description: </span>
              {project.description}
            </p>
          ) : null}
          {project.start_date ? (
            <p className="projectStartDate">
              <span className="property">Start date: </span>
              {new Date(project.start_date).toDateString()}
            </p>
          ) : null}
          {project.end_date ? (
            <p className="projectEndDate">
              <span className="property">End date: </span>
              {new Date(project.end_date).toDateString()}
            </p>
          ) : null}
          <p className="projectTypeOfPayment">
            <span className="property">Type of payment: </span>
            {type_of_payment} 
          </p>
          <p className="projectStatus">
            <span className="property">Status:</span>
            {project.status ? "" : "not"} active
          </p>
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

export default Project;
