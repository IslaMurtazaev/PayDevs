import monthPaymentActionTypes from "../constants/monthPayment";
import monthPaymentService from "../service/monthPayment";
import { history } from "../index";

export default {
  getAll,
  create,
  remove
}

function getAll(projectId) {
  return dispatch => {
    monthPaymentService.getAll(projectId).then(monthPayments => {
      dispatch({ type: monthPaymentActionTypes.ADD_ALL, monthPayments });
    });
  };
}

function create(projectId, values) {
  return dispatch => {
    monthPaymentService.create(projectId, values).then(monthPayment => {
      dispatch({ type: monthPaymentActionTypes.CREATE, monthPayment })
    })
  }
}

function remove(monthPaymentId) {
  return dispatch => {
    monthPaymentService.remove(monthPaymentId).then(response => {
      dispatch({ type: monthPaymentActionTypes.REMOVE, monthPaymentId })
    })
  }
}
