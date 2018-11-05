import { projectActionTypes } from "../constants/project";

export function project(state = {}, action) {
  switch (action.type) {
    case projectActionTypes.GET:
      return action.project;
    case projectActionTypes.UPDATE:
      return action.project;
    default:
      return state;
  }
}

export function projects(state = [], action) {
  switch (action.type) {
    case projectActionTypes.ADD_ALL:
      return [...action.projects];
    case projectActionTypes.CLEAR_ALL:
      return [];
    case projectActionTypes.CREATE:
      return state.concat([action.project]);
    case projectActionTypes.REMOVE:
      return state.filter(project => project.id !== action.id)
    case projectActionTypes.UPDATE:
      return state.map(
        project => (project.id === action.project.id ? action.project : project)
      );
    default:
      return state;
  }
}
