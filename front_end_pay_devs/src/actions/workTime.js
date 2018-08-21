import { workTimeService } from "../service/workTime";
import { workTimeConstant } from "../constants/workTime";
import { history } from "../index";

export default {
  create,
  getAll,
  update,
  remove
};

function create(values) {
  return dispatch => {
    workTimeService
      .create(values)
      .then(workTime => {
        dispatch({ type: workTimeConstant.CREATE, workTime });
      })
      .catch(error => {
        alert(error);
      });
  };
}

function getAll(hourPaymentId) {
  return dispatch => {
    workTimeService.getAll(hourPaymentId).then(workTimes => {
      dispatch({ type: workTimeConstant.GET_ALL, workTimes });
    });
  };
}

function update(projectId, hourPaymentId, workTimeId, values) {
    return dispatch => {
      workTimeService
      .update(projectId, hourPaymentId, workTimeId, values)
      .then(workTime => {
        dispatch({ type: workTimeConstant.UPDATE, workTime });
        history.push(
          `/project/${projectId}/Hourly/${hourPaymentId}/workTime`
        );
      });
    };
  }

function remove(workTimeId) {
  return dispatch => {
    workTimeService.remove(workTimeId).then(workTime => {
      dispatch({ type: workTimeConstant.REMOVE, workTime });
    });
  };
}
