import { HourPaymentConstant } from "../constants/hourPayment";

const initialStateHour = {};

export function hourPayment(state = initialStateHour, action) {
  switch(action.type) {
    case HourPaymentConstant.CREATE:
      return action.hourPayment;
    case HourPaymentConstant.GET:
      return action.hourPayment;
    default:
      return state;
  }
}

const initialStateTasks = [];

export function hourPayments(state = initialStateTasks, action) {
  switch(action.type) {
    case HourPaymentConstant.CREATE:
      return state.concat([action.hourPayment]);
    case HourPaymentConstant.GET_ALL:
      return action.hourPayments;
    case HourPaymentConstant.DELETE:
      return state.filter(hourPayment=>hourPayment.id !== action.hourPayment.id);
    default:
      return state;
  }
}