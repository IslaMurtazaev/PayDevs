import { ProjectConstant } from "../constants/project";

const initialState = [];

export default function projects(state = initialState, action) {
  switch (action.type) {
    case ProjectConstant.ADD_ALL_PROJECTS:
      return [...action.projects];
    case ProjectConstant.CLEAR_ALL_PROJECTS:
      return [];
    default:
      return state;
  }
}
