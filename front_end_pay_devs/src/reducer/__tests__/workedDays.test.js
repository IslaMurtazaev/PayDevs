import workedDays from "../workedDays";
import { workedDayActionTypes } from "../../constants/workedDay";

describe("workedDay reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(workedDays(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedWorkedDays = [{ id: 1 }, { id: 2 }, { id: 3 }];
    const action = {
      type: workedDayActionTypes.ADD_ALL,
      workedDays: retrievedWorkedDays
    };

    let result = workedDays([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedWorkedDays);
  });

  it("triggers CREATE", () => {
    const state = [{ id: 1 }, { id: 2 }, { id: 3 }];
    const createdWorkedDay = { id: 4 };
    const action = {
      type: workedDayActionTypes.CREATE,
      workedDay: createdWorkedDay
    };

    let result = workedDays(state, action);
    expect(result).toEqual([{ id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }]);
  });

  it("triggers UPDATE", () => {
    const state = [
      { id: 1, paid: false },
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ];
    const updatedWorkedDay = { id: 1, paid: true };
    const action = {
      type: workedDayActionTypes.UPDATE,
      workedDay: updatedWorkedDay
    };

    let result = workedDays(state, action);
    expect(result).toEqual([
      { id: 1, paid: true },
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ]);
  });

  it("triggers REMOVE", () => {
    const state = [
      { id: 1, paid: true },
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ];
    const removedWorkedDayId = 1

    const action = {
      type: workedDayActionTypes.REMOVE,
      workedDayId: removedWorkedDayId
    };

    let result = workedDays(state, action);
    expect(result).toEqual([
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ]);
  });
});
