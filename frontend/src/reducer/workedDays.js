import { workedDayActionTypes } from "../constants/workedDay";

const initialState = [];

export default function workedDays(state = initialState, action) {
  switch (action.type) {
    case workedDayActionTypes.ADD_ALL:
      return [...action.workedDays];
    case workedDayActionTypes.CREATE:
      return state.concat([action.workedDay]);
    case workedDayActionTypes.REMOVE:
      return state.filter(workedDay => workedDay.id !== action.workedDayId);
    case workedDayActionTypes.UPDATE:
      return state.map(
        workedDay =>
          workedDay.id === action.workedDay.id ? action.workedDay : workedDay
      );
    default:
      return state;
  }
}
