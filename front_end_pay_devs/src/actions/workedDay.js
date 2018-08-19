import workedDayActionTypes from "../constants/workedDay";
import workedDayService from "../service/workedDay";
import { history } from "../index";

export default {
  create,
  getAll,
  remove
};

function create(projectId, monthPaymentId, values) {
  return dispatch => {
    workedDayService
      .create(projectId, monthPaymentId, values)
      .then(workedDay => {
        dispatch({ type: workedDayActionTypes.CREATE_WORKED_DAY, workedDay });
        history.push(`/project/${projectId}/Monthly/${monthPaymentId}/workedDays`);
      });
  };                                              
}

function getAll(monthPaymentId) {
  return dispatch => {
    workedDayService.getAll(monthPaymentId).then(workedDays => {
      dispatch({ type: workedDayActionTypes.ADD_ALL_WORKED_DAYS, workedDays });
    });
  };
}

function remove(workedDayId) {
  return dispatch => {
    workedDayService.remove(workedDayId).then(response => {
      dispatch({ type: workedDayActionTypes.REMOVE_WORKED_DAY });
    });
  };
}
