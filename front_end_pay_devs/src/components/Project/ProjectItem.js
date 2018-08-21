import React, { Component } from "react";
import { connect } from "react-redux";
import { projectActions } from "../../actions/project";
import { Redirect, Link } from "react-router-dom";
import { history } from "../../index";
import Tasks from "../../components/Task/Tasks";
import HourPayments from "../../components/HourPayment/HourlyRates";
import MonthRates from "../MonthPayment/MonthlyRates";

class ProjectItem extends Component {
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
        sessionsType = <HourPayments project={project} />;
        break;
      case "T_P":
        type_of_payment = "Taskly";
        sessionsType = <Tasks project={project} />;
        break;
      default:
        break;
    }
    return (
      <div className="container">
      
      <h1 className="projectTitle">{project.title}</h1>
        <div className="properties">
        {project.description ? (
          <h4 ><span className="property">Description:</span> {project.description}</h4>
        ) : null}
        {project.start_date ? (
          <h4><span className="property">Start date:</span>{new Date(project.start_date).toDateString()}</h4>
        ) : null}
        {project.end_date ? (
          <h4><span className="property">End date:</span>{new Date(project.end_date).toDateString()}</h4>
        ) : null}
        <h4><span className="property">Type of payment:</span> {type_of_payment}</h4>
        <h4><span className="property">Status:</span>{project.status ? "" : "not"} active</h4>
        </div>

        <div  className="btn-group-horizontal ">

        <button type = "button" className="btn btn-success btn-lg"
          onClick={() => this.props.getTotal(project.id)}>
         Total
        </button>
        
        <Link to={`${history.location.pathname}/update`}>
          <button type = "button" className="btn btn-primary btn-lg">
            Update project
          </button>
        </Link>

          <button type="button" className="btn btn-danger btn-lg"
            onClick={() => this.props.removeProject(project.id)}>
            Delete project
          </button>
          </div>
          

          <div className="session">

  {sessionsType}
        {/* <button className="btn btn-success">
          <Link to={`/project/${project.id}/${type_of_payment}/create`}>
            Create new 
            {type_of_payment === " Taskly"
              ? "task"
              : ` ${type_of_payment.toLowerCase()} rate`}
          </Link>
        </button>
        </div>
        </button> */}
      </div>
      );</div> 
      )
  }
}

const mapStateToProps = (state, ownProps) => {
  let project = state.projects.find(
    project => project.id === Number(ownProps.match.params.id)
  );
  return {
    project
  };
};

export default connect(
  mapStateToProps,
  dispatch => ({
    removeProject: id => {
      dispatch(projectActions.remove(id));
    },
    getTotal: id => {
      dispatch(projectActions.getTotal(id));
    }
  })
)(ProjectItem);
