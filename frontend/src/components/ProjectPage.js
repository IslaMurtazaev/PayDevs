import React, { Component } from "react";
import { Link } from "react-router-dom";

class ProjectPage extends Component {
  componentDidMount() {
    this.props.getAllProjects();
  }

  render() {
    const { user } = this.props.user;
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

export default ProjectPage;
