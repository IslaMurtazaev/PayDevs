import { taskService } from "../service/task";
import {TaskConstant} from '../constants/task'
import {history} from '../index';

export const tasklyActions = {
    create,
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