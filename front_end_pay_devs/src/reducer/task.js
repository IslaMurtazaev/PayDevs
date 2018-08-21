import { TaskConstant } from "../constants/task";

const initialStateTask = {};

export function task(state = initialStateTask, action) {
  switch(action.type) {
    case TaskConstant.CREATE_TASK:
      return action.task;
    case TaskConstant.GET_TASK:
      return action.task;
    default:
      return state;
  }
}

const initialStateTasks = [];

export function tasks(state = initialStateTasks, action) {
  switch(action.type) {
    case TaskConstant.CREATE_TASK:
      return state.concat([action.task]);
    case TaskConstant.GET_ALL_TASK:
      return action.tasks;
    case TaskConstant.DELETE_TASK:
      return state.filter(task=>task.id !== action.task.id);
    default:
      return state;
  }
}