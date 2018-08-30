import configureStore from "redux-mock-store";
import thunk from "redux-thunk";

import workTimeActions from "../workTime";
import { workTimeActionTypes } from "../../constants/workTime";
import { workTimeService } from "../../service/workTime";
jest.mock("../../service/workTime.js");
jest.mock("../../index.js", () => require("history"));

const middlewares = [thunk];
const mockStore = configureStore(middlewares);
const store = mockStore({ hourPayments: [] });

describe("workTime's action creators", () => {
  afterEach(() => {
    store.clearActions();
  });

  it("creates ADD_ALL_WORK_TIME action after fetching is done", () => {
    const fetchedWorkTimes = [
      {
        id: 1,
        start_date: "1999-08-24T00:00:00.000Z",
        end_date: "1999-09-24T00:00:00.000Z",
        paid: true
      },
      {
        id: 2,
        start_date: "2018-08-30T10:00:00.000Z",
        end_date: "2018-09-24T00:00:00.000Z",
        paid: false
      }
    ];

    workTimeService.getAll.mockReturnValue(
      Promise.resolve(fetchedWorkTimes)
    );

    const expectedActions = [
      {
        type: workTimeActionTypes.ADD_ALL,
        workTimes: fetchedWorkTimes
      }
    ];

    return store.dispatch(workTimeActions.getAll(1)).then(() => {
      expect(workTimeService.getAll).toHaveBeenCalled();
      expect(workTimeService.getAll).toBeCalledWith(1);
      expect(store.getActions()).toEqual(expectedActions);
    });
  });

  it("creates CREATE_WORK_TIME action after new workTime is created", () => {
    const createdWorkTime = {
      id: 1,
      start_date: "1999-08-24T00:00:00.000Z",
      end_date: "1999-09-24T00:00:00.000Z",
      paid: true
    };

    workTimeService.create.mockReturnValue(
      Promise.resolve(createdWorkTime)
    );

    const expectedActions = [
      {
        type: workTimeActionTypes.CREATE,
        workTime: createdWorkTime
      }
    ];

    return store
      .dispatch(workTimeActions.create(createdWorkTime))
      .then(() => {
        expect(workTimeService.create).toHaveBeenCalled();
        expect(workTimeService.create).toBeCalledWith(createdWorkTime);
        expect(store.getActions()).toEqual(expectedActions);
      });
  });

  it("creates UPDATE_WORK_TIME action after new workTime is updated", () => {
    const updatedWorkTime = {
      id: 1,
      start_date: "1999-08-24T00:00:00.000Z",
      end_date: "1999-09-24T00:00:00.000Z",
      paid: true
    };

    workTimeService.update.mockReturnValue(
      Promise.resolve(updatedWorkTime)
    );

    const expectedActions = [
      {
        type: workTimeActionTypes.UPDATE,
        workTime: updatedWorkTime
      }
    ];

    return store
      .dispatch(workTimeActions.update(1, 1, 1, updatedWorkTime))
      .then(() => {
        expect(workTimeService.update).toHaveBeenCalled();
        expect(workTimeService.update).toBeCalledWith(1, 1, 1, updatedWorkTime);
        expect(store.getActions()).toEqual(expectedActions);
      });
  });

  it("creates REMOVE_WORK_TIME action after removing workTime", () => {
    const removedWorkTimeId = 1;

    workTimeService.remove.mockReturnValue(
      Promise.resolve(removedWorkTimeId)
    );

    const expectedActions = [
      {
        type: workTimeActionTypes.REMOVE,
        workTimeId: removedWorkTimeId
      }
    ];

    return store
      .dispatch(workTimeActions.remove(removedWorkTimeId))
      .then(() => {
        expect(workTimeService.remove).toHaveBeenCalled();
        expect(workTimeService.remove).toBeCalledWith(removedWorkTimeId);
        expect(store.getActions()).toEqual(expectedActions);
      });
  });
});
