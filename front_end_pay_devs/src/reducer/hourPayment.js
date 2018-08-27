import { hourPaymentActionTypes } from "../constants/hourPayment";

const initialStateHour = {};

export function hourPayment(state = initialStateHour, action) {
  switch(action.type) {
    case hourPaymentActionTypes.CREATE:
      return action.hourPayment;
    default:
      return state;
  }
}

const initialStateTasks = [];

export function hourPayments(state = initialStateTasks, action) {
  switch(action.type) {
    case hourPaymentActionTypes.CREATE:
      return state.concat([action.hourPayment]);
    case hourPaymentActionTypes.ADD_ALL:
      return action.hourPayments;
    case hourPaymentActionTypes.REMOVE:
      return state.filter(hourPayment=>hourPayment.id !== action.hourPaymentId);
    default:
      return state;
  }
}