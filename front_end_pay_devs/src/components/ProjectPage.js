import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { projectActions } from "../actions/project";

class ProjectPage extends Component {
  onClick() {
    this.props.onGetAllProjects();
  }

  componentDidMount() {
    this.props.onGetAllProjects();
  }

  render() {
    const { user } = this.props.user;
    const { projects } = this.props;

    return (
      <div>
        {user && <div> Username: {user.username}</div>}
        {user && <div> Email: {user.email}</div>}
        {user && <Link to="/login">Logout</Link>}
        <ul>
          {projects.map(project => (
            <li key={project.id}>
              <Link to={`/project/${project.id}`}>{project.title}</Link>
            </li>
          ))}
        </ul>
        <Link to={"/project/create"}>New project</Link>
      </div>
    );
  }
}

export default connect(
  state => ({
    user: state.user,
    projects: state.projects
  }),
  dispatch => ({
    onGetAllProjects: () => {
      dispatch(projectActions.getAll());
    },
    onClearProjects: () => {
      dispatch(projectActions.clearAll());
    }
  })
)(ProjectPage);
