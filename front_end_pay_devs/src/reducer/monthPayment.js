import monthPaymentActionTypes from "../constants/monthPayment";

const initialState = {};

export default function monthPayment(state = initialState, action) {
  switch (action.type) {
    case monthPaymentActionTypes.CREATE:
      return action.monthPayment;
    default:
      return state;
  }
}
