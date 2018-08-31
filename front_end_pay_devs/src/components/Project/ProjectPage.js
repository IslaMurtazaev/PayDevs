import React, { Component } from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { projectActions } from "../../actions/project";

class ProjectPage extends Component {
  componentWillMount() {
    if (!this.props.projects.length) this.props.getAllProjects();
  }

  render() {
    const { user } = this.props.user; // why we are wrapping user inside a user?
    const { projects } = this.props;
    return (
      <div>
        <div className="user">
          {user && <div className="username">{user.username}</div>}
          {user && <div className="email">{user.email}</div>}
        </div>
        <Link className="newProjectLink" to="/project/create">
          New Project
        </Link>
        <div className="projectList">
          <ul>
            {projects.map(project => (
              <li key={project.id}>
                <div className="projectInfo">
                  <Link className="projectLink" to={`/project/${project.id}`}>
                    {project.title}
                  </Link>
                  <p>{new Date(project.start_date).toDateString()}</p>
                </div>
              </li>
            ))}
          </ul>
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
    getAllProjects: () => {
      dispatch(projectActions.getAll());
    }
  })
)(ProjectPage);
