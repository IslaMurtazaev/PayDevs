import { projectService } from "../service/project";
import { ProjectConstant } from "../constants/project";
import {history} from '../index'

export const projectActions = {
    getAll,
    clearAll,
    deleteProject
};

function getAll(){
    return dispatch=>{
        projectService.get_all().then((projects) =>
            {
                dispatch({type: ProjectConstant.ADD_ALL_PROJECTS, projects});
            },    
      
        )
    }
}

function clearAll(){
    return {type: ProjectConstant.CLEAR_ALL_PROJECTS}
    
}

function deleteProject(id){
    return dispatch=>{
        projectService.deleteProject(id).then(() =>
            {
                dispatch({type: ProjectConstant.DELETE_PROJECT});
                history.push('/');
            },    
      
        )
    }
}