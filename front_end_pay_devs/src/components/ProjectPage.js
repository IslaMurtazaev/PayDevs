import React, { Component } from 'react';
import {connect} from 'react-redux';
import {Link} from 'react-router'
import { projectActions } from '../actions/project';


class ProjectPage extends Component {

  onClick(){
    this.props.onGetAllProjects();
  }
  componentWillUnmount() {
   
    this.props.onClearProjects();
  }

  render() {
    const {user, error} = this.props.user;
    const {projects} = this.props;
    
    console.log(projects, 'projects')
    // console.log(user, 'user')
    // console.log(error, 'error')
    return (
      <div>   
          {error && <div>{error.error.message}</div>}
          {user && <div> Username: {user.username}</div>}
          {user && <div> Email: {user.email}</div>}
          {user &&<Link to="/login">Logout</Link>}

          {user && <div><button onClick={this.onClick.bind(this)}>Get All Projects</button></div>}
         
          {projects && <ul>{projects.map(project => <li key={project.id}>{project.title}</li>)}</ul>}
          
      </div>
    );
  }
}

export default connect(
    (state) => ({
      user: state.user,
      error: state.error,
      projects: state.projects,
    }),
    dispatch =>({
      onGetAllProjects:() => {
        dispatch(projectActions.getAll())
      },
      onClearProjects:() => {
        dispatch(projectActions.clearAll())
      },

    })
)(ProjectPage);
