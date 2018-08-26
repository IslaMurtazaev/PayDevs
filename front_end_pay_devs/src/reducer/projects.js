import { ProjectConstants } from "../constants/project";

export function project(state = {}, action) {
  switch (action.type) {
    case ProjectConstants.GET_PROJECT:
      return action.project
    default:
      return state;
  }
}

export function projects(state = [], action) {
  switch (action.type) {
    case ProjectConstants.ADD_ALL_PROJECTS:
      return [...action.projects];
    case ProjectConstants.CLEAR_ALL_PROJECTS:
      return [];
    case ProjectConstants.CREATE_PROJECT:
      return state.concat([action.project]);
    case ProjectConstants.UPDATE_PROJECT:
      return state.map(
        project => project.id === action.project.id ? action.project : project
      );   
    default:
      return state;
  }
}
