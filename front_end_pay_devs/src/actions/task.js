import { taskService } from "../service/task";
import { taskActionTypes } from "../constants/task";
import { history } from "../index";
import { handleError } from "../service/helpers";

export const tasklyActions = {
  create,
  getAll,
  remove,
  update
};

function create(task, projectId) {
  return dispatch =>
    taskService
      .create(task, projectId)
      .then(task => dispatch({ type: taskActionTypes.CREATE, task }))
      .catch(error => handleError(error));
}

function getAll(projectId) {
  return dispatch =>
    taskService
      .getAll(projectId)
      .then(tasks => dispatch({ type: taskActionTypes.ADD_ALL, tasks }))
      .catch(error => handleError(error));
}

function remove(taskId) {
  return dispatch =>
    taskService
      .remove(taskId)
      .then(task => {
        dispatch({ type: taskActionTypes.REMOVE, taskId });
      })
      .catch(error => handleError(error));
}

function update(values) {
  return dispatch =>
    taskService
      .update(values)
      .then(task => {
        dispatch({ type: taskActionTypes.UPDATE, task });
        history.push(`/project/${values.projectId}`);
      })
      .catch(error => handleError(error));
}
