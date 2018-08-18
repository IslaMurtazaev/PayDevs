import { ProjectConstant } from "../constants/project";

const initialState = [];

export default function projects(state = initialState, action) {
  switch (action.type) {
    case ProjectConstant.ADD_ALL_PROJECTS:
      return [...action.projects];
    case ProjectConstant.CLEAR_ALL_PROJECTS:
      return [];
    case ProjectConstant.CREATE_PROJECT:
      return state.concat([action.project]);
    case ProjectConstant.UPDATE_PROJECT:
      return state.map(
        project => project.id === action.project.id ? action.project : project
      );   
    default:
      return state;
  }
}
