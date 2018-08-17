import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../actions/project";
import { Redirect, Link, NavLink } from "react-router-dom";
import { history } from "../index";

class ProjectItem extends Component {
  onClick(id) {
    this.props.onGetAllProjects(id);
  }

  onClickTotal(id) {
    this.props.onGetTotal(id);
  }

  render() {
    let project = this.props.project;

    if (!Object.keys(project).length)
      return <Redirect from="/project/:id" to="/" />;

    let sessionsType;
    let type_of_payment;
    switch (project.type_of_payment) {
      case "M_P":
        type_of_payment = "Monthly";
        sessionsType = <div>Month rates list</div>
        break;
      case "H_P":
        type_of_payment = "Hourly";
        sessionsType = <div>Hour rates list</div>
        break;
      case "T_P":
        type_of_payment = "Taskly";
        sessionsType = <div>Tasks list</div>
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

        <NavLink to={`${history.location.pathname}/update`}>
          <button className="btn btn-warning">Update project</button>
        </NavLink>

        <button
          className="btn btn-danger"
          onClick={this.onClickTotal.bind(this, project.id)}
        >
          Total
        </button>

        <button className="btn btn-danger">
          <Link to={`/project/${project.id}/${type_of_payment}/create`}>
            Create {type_of_payment.toLowerCase()} session
          </Link>
        </button>

        <button
          className="btn btn-danger"
          onClick={this.onClick.bind(this, project.id)}
        >
          Delete project
        </button>

        {sessionsType}
      </div>
    );
  }
}

const mapStateToProps = (state, ownProps) => {
  let project = state.projects.find(
    product => product.id === Number(ownProps.match.params.id)
  );
  return {
    project: project ? project : state.project
  };
};

export default connect(
  mapStateToProps,
  dispatch => ({
    onGetAllProjects: id => {
      dispatch(projectActions.deleteProject(id));
    },
    onGetTotal: id => {
      dispatch(projectActions.getTotal(id));
    }
  })
)(ProjectItem);
