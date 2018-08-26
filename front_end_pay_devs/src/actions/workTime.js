import { workTimeService } from "../service/workTime";
import { WorkTimeConstants } from "../constants/workTime";
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
        dispatch({ type: WorkTimeConstants.CREATE, workTime });
      })
      .catch(error => handleError(error));
  };
}

function getAll(hourPaymentId) {
  return dispatch => {
    workTimeService.getAll(hourPaymentId).then(workTimes => {
      dispatch({ type: WorkTimeConstants.ADD_ALL, workTimes });
    });
  };
}

function update(projectId, hourPaymentId, workTimeId, values) {
  return dispatch => {
    workTimeService
      .update(projectId, hourPaymentId, workTimeId, values)
      .then(workTime => {
        dispatch({ type: WorkTimeConstants.UPDATE, workTime });
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
        dispatch({ type: WorkTimeConstants.REMOVE, workTimeId });
      })
      .catch(error => handleError(error));
  };
}
