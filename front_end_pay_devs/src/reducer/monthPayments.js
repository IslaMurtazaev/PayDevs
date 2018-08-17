import monthPaymentActionTypes from "../constants/monthPayment";

const initialState = [];

export default function monthPayment(state = initialState, action) {
  switch (action.type) {
    case monthPaymentActionTypes.ADD_ALL:
      return [...action.monthPayments];
    case monthPaymentActionTypes.REMOVE:
      return state.filter(monthPayment => monthPayment.id !== action.monthPaymentId)
    default:
      return state;
  }
}
