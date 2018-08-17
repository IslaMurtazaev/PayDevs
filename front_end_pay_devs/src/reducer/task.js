import { TaksConstant } from "../constants/task";

const initialState = {};

export default function projects(state = initialState, action) {
  switch(action.type) {
    case TaksConstant.CREATE_TASK:
      return action.task;
    default:
      return state;
  }
}