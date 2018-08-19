import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { projectActions } from "../../actions/project";
import logo from '../icons/favicon.png';

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
        <div className="logoutLink">
          <img src={logo} />          
          <span className="projectName">PayDevs</span>
          {user && <Link className="link" to="/login">Logout</Link>}
        </div>
        {user && <div> Username: {user.username}</div>}
        {user && <div> Email: {user.email}</div>}
       
        <ul>
          {projects.map(project => (
            <li key={project.id}>
              <Link className="link" to={`/project/${project.id}`}>{project.title}</Link>
            </li>
          ))}
        </ul>
        <Link className="link" to="/project/create">New project</Link>
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
