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
          <span className="paydevs1">PayDevs</span>
          {user && <Link className="link" to="/login">Logout</Link>}
        </div>
        <div className="user">
        {user && <div className="username"> {user.username}</div>}
        {user && <div className="email">{user.email}</div>}
        </div>
        <h3 className="projects">Projects</h3>
       <div className="projectList">
          {projects.map(project => (
            <div className="projectInfo">
            <li key={project.id}>
              <Link className="projectLink" to={`/project/${project.id}`}>{project.title}</Link>
            </li> <br/>              
            <p>{project.start_date}</p>
            </div>
          ))}
        <Link className="newProjectLink" to="/project/create">New project</Link>
        </div>
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
