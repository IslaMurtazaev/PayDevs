import { TaskConstants } from "../constants/task";

const initialStateTask = {};

export function task(state = initialStateTask, action) {
  switch (action.type) {
    case TaskConstants.CREATE_TASK:
      return action.task;
    default:
      return state;
  }
}

const initialStateTasks = [];

export function tasks(state = initialStateTasks, action) {
  switch (action.type) {
    case TaskConstants.CREATE_TASK:
      return [...state, action.task];
    case TaskConstants.UPDATE_TASK:
      return state.map(task => task.id !== action.task.id ? task : action.task);
    case TaskConstants.ADD_ALL_TASKS:
      return [...action.tasks];
    case TaskConstants.DELETE_TASK:
      return state.filter(task => task.id !== action.task.id);
    default:
      return state;
  }
}
