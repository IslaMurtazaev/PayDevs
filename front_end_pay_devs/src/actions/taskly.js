import { taskService } from "../service/task";
import {TaskConstant} from '../constants/task'
import {history} from '../index';

export const tasklyActions = {
    create,
    getAll,
    taksDelete,
    update
  };
  

  function create(task, projectId) {
    return dispatch => {
      taskService
        .create(task, projectId)
        .then(task => {
          dispatch({ type: TaskConstant.CREATE_TASK, task });
          history.push(`/project/${projectId}`)
        })
        .catch(error => {
          alert(error);
        });
    };
  }

  function getAll(projectId) {
    return dispatch => {
      taskService.getAll(projectId).then(tasks => {
        dispatch({ type: TaskConstant.GET_ALL_TASK, tasks });
      });
    };
  }
  

  function taksDelete(taksId) {
    return dispatch => {
      taskService.taksDelete(taksId).then(task => {
        dispatch({ type: TaskConstant.DELETE_TASK, task});
      });
    };
  }

  function update(values){
    return dispatch => {
      taskService
          .update(values)
          .then(task => {
            dispatch({ type: TaskConstant.CREATE_TASK, task });
            history.push(`/project/${values.projectId}`)
          })
          .catch(error => {
            alert(error);
          });
      }
    }
  