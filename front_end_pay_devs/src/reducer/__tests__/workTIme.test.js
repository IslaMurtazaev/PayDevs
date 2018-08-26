import { workTime, workTimes } from "../workTime";
import { workTimeActionTypes } from "../../constants/workTime";

describe("workTime reducer", () => {
  it("has a default state", () => {
    const defaultState = {};
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(workTime(undefined, action)).toEqual(defaultState);
  });

  it("triggers CREATE", () => {
    const createdWorkTime = {
      paid: false
    };
    const action = {
      type: workTimeActionTypes.CREATE,
      workTime: createdWorkTime
    };

    expect(workTime({}, action)).toBe(createdWorkTime);
  });
});

describe("workedDay reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(workTimes(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedWorkTime = [{ id: 1 }, { id: 2 }, { id: 3 }];
    const action = {
      type: workTimeActionTypes.ADD_ALL,
      workTimes: retrievedWorkTime
    };

    let result = workTimes([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedWorkTime);
  });

  it("triggers CREATE", () => {
    const state = [{ id: 1 }, { id: 2 }, { id: 3 }];
    const createdWorkTime = { id: 4 };
    const action = {
      type: workTimeActionTypes.CREATE,
      workTime: createdWorkTime
    };

    let result = workTimes(state, action);
    expect(result).toEqual([{ id: 1 }, { id: 2 }, { id: 3 }, { id: 4 }]);
  });

  it("triggers UPDATE", () => {
    const state = [
      { id: 1, paid: false },
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ];
    const updatedWorkTime = { id: 1, paid: true };
    const action = {
      type: workTimeActionTypes.UPDATE,
      workTime: updatedWorkTime
    };

    let result = workTimes(state, action);
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
    const removedWorkTimeId = 1;

    const action = {
      type: workTimeActionTypes.REMOVE,
      workTimeId: removedWorkTimeId
    };

    let result = workTimes(state, action);
    expect(result).toEqual([
      { id: 2, paid: false },
      { id: 3, paid: false },
      { id: 4, paid: false }
    ]);
  });
});
