import { ProjectConstant } from "../constants/project";

const initialState = {};

export default function projects(state = initialState, action) {
  switch(action.type) {
    case ProjectConstant.CREATE_PROJECT:
      return action.project;
    case ProjectConstant.UPDATE_PROJECT:
      return action.project;
    default:
      return state;
  }
}
