import { WorkTimeConstants } from "../constants/workTime";

const initialStateHour = {};

export function workTime(state = initialStateHour, action) {
  switch (action.type) {
    case WorkTimeConstants.CREATE:
      return action.workTime;
    default:
      return state;
  }
}

const initialStateworkTimes = [];

export function workTimes(state = initialStateworkTimes, action) {
  switch (action.type) {
    case WorkTimeConstants.ADD_ALL:
      return action.workTimes;
    case WorkTimeConstants.CREATE:
      return [...state, action.workTime];
    case WorkTimeConstants.UPDATE:
      return state.map(
        workTime =>
          workTime.id !== action.workTime.id ? workTime : action.workTime
      );
    case WorkTimeConstants.REMOVE:
      return state.filter(workTime => workTime.id !== action.workTimeId);
    default:
      return state;
  }
}
