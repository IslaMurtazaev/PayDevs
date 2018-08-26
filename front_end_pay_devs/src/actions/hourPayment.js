import { hourPaymentService } from "../service/hourPayment";
import { HourPaymentConstants } from "../constants/hourPayment";
import { history } from "../index";
import { handleError } from "../service/helpers";

export const hourPaymentActions = {
  getAll,
  create,
  remove,
  update
};

function getAll(projectId) {
  return dispatch => {
    hourPaymentService.getAll(projectId).then(hourPayments => {
      dispatch({ type: HourPaymentConstants.ADD_ALL, hourPayments });
    });
  };
}

function create(hourPayment) {
  return dispatch => {
    hourPaymentService
      .create(hourPayment)
      .then(hourPayment => {
        dispatch({ type: HourPaymentConstants.CREATE, hourPayment });
      })
      .catch(error => handleError(error));
  };
}

function remove(hourPaymentId) {
  return dispatch => {
    hourPaymentService
      .remove(hourPaymentId)
      .then(hourPayment => {
        dispatch({ type: HourPaymentConstants.REMOVE, hourPaymentId });
      })
      .catch(error => handleError(error));
  };
}

function update(values) {
  return dispatch => {
    hourPaymentService
      .update(values)
      .then(hourPayment => {
        dispatch({ type: HourPaymentConstants.CREATE, hourPayment });
        history.push(`/project/${values.projectId}`);
      })
      .catch(error => handleError(error));
  };
}
