import { taskService } from "../service/task";
import { TaskConstants } from "../constants/task";
import { history } from "../index";
import { handleError } from "../service/helpers";

export const tasklyActions = {
  create,
  getAll,
  remove,
  update
};

function create(task, projectId) {
  return dispatch => {
    taskService
      .create(task, projectId)
      .then(task => {
        dispatch({ type: TaskConstants.CREATE_TASK, task });
      })
      .catch(error => handleError(error));
  };
}

function getAll(projectId) {
  return dispatch => {
    taskService
      .getAll(projectId)
      .then(tasks => {
        dispatch({ type: TaskConstants.ADD_ALL_TASKS, tasks });
      })
      .catch(error => handleError(error));
  };
}

function remove(taskId) {
  return dispatch => {
    taskService
      .remove(taskId)
      .then(task => {
        dispatch({ type: TaskConstants.DELETE_TASK, task });
      })
      .catch(error => handleError(error));
  };
}

function update(values) {
  return dispatch => {
    taskService
      .update(values)
      .then(task => {
        dispatch({ type: TaskConstants.UPDATE_TASK, task });
        history.push(`/project/${values.projectId}`);
      })
      .catch(error => handleError(error));
  };
}
