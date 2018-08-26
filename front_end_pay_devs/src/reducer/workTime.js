import { workTimeActionTypes } from "../constants/workTime";

const initialStateHour = {};

export function workTime(state = initialStateHour, action) {
  switch (action.type) {
    case workTimeActionTypes.CREATE:
      return action.workTime;
    default:
      return state;
  }
}

const initialStateworkTimes = [];

export function workTimes(state = initialStateworkTimes, action) {
  switch (action.type) {
    case workTimeActionTypes.ADD_ALL:
      return action.workTimes;
    case workTimeActionTypes.CREATE:
      return [...state, action.workTime];
    case workTimeActionTypes.UPDATE:
      return state.map(
        workTime =>
          workTime.id !== action.workTime.id ? workTime : action.workTime
      );
    case workTimeActionTypes.REMOVE:
      return state.filter(workTime => workTime.id !== action.workTimeId);
    default:
      return state;
  }
}
