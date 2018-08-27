import monthPayments from "../monthPayments";
import { monthPaymentActionTypes } from "../../constants/monthPayment";

describe("monthPayments reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(monthPayments(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedMonthPayments = [
      { rate: 100 },
      { rate: 200 },
      { rate: 300 }
    ];
    const action = {
      type: monthPaymentActionTypes.ADD_ALL,
      monthPayments: retrievedMonthPayments
    };

    let result = monthPayments([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedMonthPayments);
  });

  it("triggers CREATE", () => {
    const state = [
      { rate: 100 },
      { rate: 200 },
      { rate: 300 }
    ];
    const createdMonthPayment = { rate: 400 };
    const action = {
      type: monthPaymentActionTypes.CREATE,
      monthPayment: createdMonthPayment
    };

    let result = monthPayments(state, action);
    expect(result).toEqual([
      { rate: 100 },
      { rate: 200 },
      { rate: 300 },
      { rate: 400 }    
    ]);
  });

  it("triggers REMOVE", () => {
    const state = [
      { id: 1, rate: 100 },
      { id: 2, rate: 200 },
      { id: 3, rate: 300 },
      { id: 4, rate: 400 }    
    ];
    const removedMonthPaymentId = 1  

    const action = {
      type: monthPaymentActionTypes.REMOVE,
      monthPaymentId: removedMonthPaymentId
    };

    let result = monthPayments(state, action);
    expect(result).toEqual([
      { id: 2, rate: 200 },
      { id: 3, rate: 300 },
      { id: 4, rate: 400 }    
    ]);
  });
})
