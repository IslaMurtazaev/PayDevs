import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../../actions/project";
import { Redirect, Link } from "react-router-dom";
import Tasks from "../../components/Task/Tasks";
import HourPayments from "../../components/HourPayment/HourlyRates";
import MonthRates from "../MonthPayment/MonthlyRates";

class ProjectItem extends Component {
  componentDidMount() {
    this.props.getProject();
  }

  render() {
    let project = this.props.project;

    if (!project) return <Redirect from="/project/:id" to="/" />;

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
            <h4>
              <span className="property">Description:</span>{" "}
              {project.description}
            </h4>
          ) : null}
          {project.start_date ? (
            <h4>
              <span className="property">Start date:</span>
              {new Date(project.start_date).toDateString()}
            </h4>
          ) : null}
          {project.end_date ? (
            <h4>
              <span className="property">End date:</span>
              {new Date(project.end_date).toDateString()}
            </h4>
          ) : null}
          <h4>
            <span className="property">Type of payment:</span> {type_of_payment}
          </h4>
          <h4>
            <span className="property">Status:</span>
            {project.status ? "" : "not"} active
          </h4>
        </div>

        <div  className="btn-group">

        <button type = "button" className="btn btn-success btn-lg"
          onClick={() => this.props.getTotal(project.id)}>
         Total
        </button>
        
        <Link to={`project/${project.id}/update`}>
          <button type = "button" className="btn btn-warning btn-lg">
            Update
            </button>
          </Link>

          <button type="button" className="btn btn-danger btn-lg"
            onClick={() => this.props.removeProject(project.id)}>
            Delete
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
