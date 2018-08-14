import { projectService } from "../service/project";
import { ProjectConstant } from "../constants/project";

export const projectActions = {
    getAll,
    clearAll
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