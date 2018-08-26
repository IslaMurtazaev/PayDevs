import workedDays from "../workedDays";
import actionTypes from "../../constants/workedDay";

describe("workedDay reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(workedDays(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedWorkedDays = [{ id: 1 }, { id: 2 }, { id: 3 }];
    const action = {
      type: actionTypes.ADD_ALL_WORKED_DAYS,
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
      type: actionTypes.CREATE_WORKED_DAY,
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
      type: actionTypes.UPDATE_WORKED_DAY,
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
      type: actionTypes.REMOVE_WORKED_DAY,
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
