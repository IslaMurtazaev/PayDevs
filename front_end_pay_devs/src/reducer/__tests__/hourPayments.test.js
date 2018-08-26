import { hourPayment, hourPayments } from "../hourPayment";
import { HourPaymentConstants } from "../../constants/hourPayment";

describe("hourPayment reducer", () => {
  it("has a default state", () => {
    const defaultState = {};
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(hourPayment(undefined, action)).toEqual(defaultState);
  });

  it("triggers CREATE", () => {
    const createdHourPayment = { rate: 20 };
    const action = {
      type: HourPaymentConstants.CREATE,
      hourPayment: createdHourPayment
    };

    expect(hourPayment({}, action)).toBe(createdHourPayment);
  });
});

describe("hourPayments reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(hourPayments(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedHourPayments = [
      { rate: 10 },
      { rate: 20 },
      { rate: 30 }
    ];
    const action = {
      type: HourPaymentConstants.ADD_ALL,
      hourPayments: retrievedHourPayments
    };

    let result = hourPayments([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedHourPayments);
  });

  it("triggers CREATE", () => {
    const state = [{ rate: 10 }, { rate: 20 }, { rate: 30 }];
    const createdHourPayment = { rate: 40 };
    const action = {
      type: HourPaymentConstants.CREATE,
      hourPayment: createdHourPayment
    };

    let result = hourPayments(state, action);
    expect(result).toEqual([
      { rate: 10 },
      { rate: 20 },
      { rate: 30 },
      { rate: 40 }
    ]);
  });

  it("triggers REMOVE", () => {
    const state = [
      { id: 1, rate: 10 },
      { id: 2, rate: 20 },
      { id: 3, rate: 30 },
      { id: 4, rate: 40 }
    ];
    const removedHourPaymentId = 1;

    const action = {
      type: HourPaymentConstants.REMOVE,
      hourPaymentId: removedHourPaymentId
    };

    let result = hourPayments(state, action);
    expect(result).toEqual([
      { id: 2, rate: 20 },
      { id: 3, rate: 30 },
      { id: 4, rate: 40 }
    ]);
  });
});
