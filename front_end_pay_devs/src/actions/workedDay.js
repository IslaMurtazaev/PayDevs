import { workedDayActionTypes } from "../constants/workedDay";
import workedDayService from "../service/workedDay";
import { history } from "../index";
import { handleError } from "../service/helpers";

export default {
  create,
  getAll,
  remove,
  update
};

function create(projectId, monthPaymentId, values) {
  return dispatch => {
    workedDayService
      .create(projectId, monthPaymentId, values)
      .then(workedDay => {
        dispatch({ type: workedDayActionTypes.CREATE, workedDay });
        history.push(
          `/project/${projectId}/Monthly/${monthPaymentId}/workedDay`
        );
      })
      .catch(error => handleError(error));
  };
}

function getAll(monthPaymentId) {
  return dispatch => {
    workedDayService.getAll(monthPaymentId).then(workedDays => {
      dispatch({ type: workedDayActionTypes.ADD_ALL, workedDays });
    });
  };
}

function remove(workedDayId) {
  return dispatch => {
    workedDayService
      .remove(workedDayId)
      .then(response => {
        dispatch({ type: workedDayActionTypes.REMOVE, workedDayId });
      })
      .catch(error => handleError(error));
  };
}

function update(projectId, monthPaymentId, workedDayId, values) {
  return dispatch => {
    workedDayService
      .update(projectId, monthPaymentId, workedDayId, values)
      .then(workedDay => {
        dispatch({ type: workedDayActionTypes.UPDATE, workedDay });
        history.push(
          `/project/${projectId}/Monthly/${monthPaymentId}/workedDay`
        );
      })
      .catch(error => handleError(error));
  };
}
