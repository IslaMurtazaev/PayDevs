import { monthPaymentActionTypes } from "../constants/monthPayment";

const initialState = [];

export default function monthPayments(state = initialState, action) {
  switch (action.type) {
    case monthPaymentActionTypes.ADD_ALL:
      return [...action.monthPayments];
    case monthPaymentActionTypes.CREATE:
      return state.concat([action.monthPayment]);
    case monthPaymentActionTypes.REMOVE:
      return state.filter(monthPayment => monthPayment.id !== action.monthPaymentId)
    default:
      return state;
  }
}
