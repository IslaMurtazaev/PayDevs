import {ProjectConstant} from '../constants/project'

const initialState = [];

export default function projects(state=initialState, action){
    if (action.type === ProjectConstant.ADD_ALL_PROJECTS){
      return [     
        ...action.projects
      ]
      
    }else if(action.type === ProjectConstant.CLEAR_ALL_PROJECTS){
        return []
    }
    
    return state;
    
  
  }