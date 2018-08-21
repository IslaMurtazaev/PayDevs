import { hourPaymentService } from "../service/hourPayment";
import { HourPaymentConstant } from "../constants/hourPayment";
import { history } from "../index";
import {handleError} from "../service/helpers"

export const hourPaymentActions = {
  getAll,
  create,
  remove,
  update
};

function getAll(projectId) {
  return dispatch => {
    hourPaymentService.getAll(projectId).then(hourPayments => {
      dispatch({ type: HourPaymentConstant.GET_ALL, hourPayments });
    });
  };
}

function create(hourPayment) {
  return dispatch => {
    hourPaymentService
      .create(hourPayment)
      .then(hourPayment => {
        dispatch({ type: HourPaymentConstant.CREATE, hourPayment });
      }).catch(error => handleError(error));
      // .catch(error => {
      // });
  };
}

function remove(hourId) {
  return dispatch => {
    hourPaymentService.remove(hourId).then(hourPayment => {
      dispatch({ type: HourPaymentConstant.DELETE, hourPayment });
    }).catch(error => handleError(error));
  };
}

function update(values) {
  return dispatch => {
    hourPaymentService
      .update(values)
      .then(hourPayment => {
        dispatch({ type: HourPaymentConstant.CREATE, hourPayment });
        history.push(`/project/${values.projectId}`);
      }).catch(error => handleError(error));
  };
}
