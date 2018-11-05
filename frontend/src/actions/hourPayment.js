import { hourPaymentService } from "../service/hourPayment";
import { hourPaymentActionTypes } from "../constants/hourPayment";
import { handleError } from "../service/helpers";

export const hourPaymentActions = {
  getAll,
  create,
  remove
};

function getAll(projectId) {
  return dispatch =>
    hourPaymentService.getAll(projectId).then(hourPayments => {
      dispatch({ type: hourPaymentActionTypes.ADD_ALL, hourPayments });
    });
}

function create(hourPayment) {
  return dispatch =>
    hourPaymentService
      .create(hourPayment)
      .then(hourPayment => {
        dispatch({ type: hourPaymentActionTypes.CREATE, hourPayment });
      })
      .catch(error => handleError(error));
}

function remove(hourPaymentId) {
  return dispatch =>
    hourPaymentService
      .remove(hourPaymentId)
      .then(hourPayment => {
        dispatch({ type: hourPaymentActionTypes.REMOVE, hourPaymentId });
      })
      .catch(error => handleError(error));
}
