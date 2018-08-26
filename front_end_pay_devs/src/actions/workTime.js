import { workTimeService } from "../service/workTime";
import { workTimeActionTypes } from "../constants/workTime";
import { history } from "../index";
import { handleError } from "../service/helpers";

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
        dispatch({ type: workTimeActionTypes.CREATE, workTime });
      })
      .catch(error => handleError(error));
  };
}

function getAll(hourPaymentId) {
  return dispatch => {
    workTimeService.getAll(hourPaymentId).then(workTimes => {
      dispatch({ type: workTimeActionTypes.ADD_ALL, workTimes });
    });
  };
}

function update(projectId, hourPaymentId, workTimeId, values) {
  return dispatch => {
    workTimeService
      .update(projectId, hourPaymentId, workTimeId, values)
      .then(workTime => {
        dispatch({ type: workTimeActionTypes.UPDATE, workTime });
        history.push(`/project/${projectId}/Hourly/${hourPaymentId}/workTime`);
      })
      .catch(error => handleError(error));
  };
}

function remove(workTimeId) {
  return dispatch => {
    workTimeService
      .remove(workTimeId)
      .then(workTime => {
        dispatch({ type: workTimeActionTypes.REMOVE, workTimeId });
      })
      .catch(error => handleError(error));
  };
}
