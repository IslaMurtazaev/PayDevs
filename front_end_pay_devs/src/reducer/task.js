import { taskActionTypes } from "../constants/task";

const initialStateTask = {};

export function task(state = initialStateTask, action) {
  switch (action.type) {
    case taskActionTypes.CREATE:
      return action.task;
    default:
      return state;
  }
}

const initialStateTasks = [];

export function tasks(state = initialStateTasks, action) {
  switch (action.type) {
    case taskActionTypes.CREATE:
      return [...state, action.task];
    case taskActionTypes.UPDATE:
      return state.map(task => task.id !== action.task.id ? task : action.task);
    case taskActionTypes.ADD_ALL:
      return [...action.tasks];
    case taskActionTypes.REMOVE:
      return state.filter(task => task.id !== action.taskId);
    default:
      return state;
  }
}
