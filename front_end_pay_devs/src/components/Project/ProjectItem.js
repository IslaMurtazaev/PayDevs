import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../../actions/project";
import { Redirect, Link } from "react-router-dom";
import { history } from "../../index";
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
        <h3>Title: {project.title}</h3>
        {project.description ? (
          <h4>Description: {project.description}</h4>
        ) : null}
        {project.start_date ? (
          <h4>Start-date: {new Date(project.start_date).toDateString()}</h4>
        ) : null}
        {project.end_date ? (
          <h4>End-date: {new Date(project.end_date).toDateString()}</h4>
        ) : null}
        <h4>Type of payment: {type_of_payment}</h4>
        <h4>Status: {project.status ? "" : "not"} active</h4>

        <Link to={`${history.location.pathname}/update`}>
          <button className="btn btn-warning">Update project</button>
        </Link>

        <button
          className="btn btn-danger"
          onClick={() => this.props.getTotal(project.id)}
        >
          Total
        </button>

        <button
          className="btn btn-danger"
          onClick={() => this.props.removeProject(project.id)}
        >
          Delete project
        </button>

        {sessionsType}
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
