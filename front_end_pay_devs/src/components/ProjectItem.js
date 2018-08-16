import React, { Component } from 'react';
import {connect} from 'react-redux';
import {projectActions} from '../actions/project'



class ProjectItem extends Component{

    onClick(id){
        this.props.onGetAllProjects(id);
    }

    render(){
        let project = this.props.project
        if(!project) return <Redirect from='/project/:id' to="/"/>
        return (
            <div>
                <h2>{project.title}</h2>
                <p>Description: {project.description}</p>
                <p>Type of payment: {project.type_of_payment}</p>
                <p>Start date: {new Date(project.start_date).toString()}</p>
                <p>End date: {new Date(project.end_date).toString()}</p>
                <button onClick={this.onClick.bind(this, project.id)}>DELETE PROJECT</button>
            </div>
        )
    }
}

const mapStateToProps = (state, ownProps) => {
    return {
        project: state.projects.find(product=>product.id === Number(ownProps.match.params.id))
    }

}

export default connect(
    mapStateToProps,
    dispatch =>({
        onGetAllProjects:(id) => {
          dispatch(projectActions.deleteProject(id))
        }
    })
)(ProjectItem);