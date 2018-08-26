import actionTypes from "../constants/workedDay";

const initialState = [];

export default function workedDays(state = initialState, action) {
  switch (action.type) {
    case actionTypes.ADD_ALL_WORKED_DAYS:
      return [...action.workedDays];
    case actionTypes.CREATE_WORKED_DAY:
      return state.concat([action.workedDay]);
    case actionTypes.REMOVE_WORKED_DAY:
      return state.filter(workedDay => workedDay.id !== action.workedDayId);
    case actionTypes.UPDATE_WORKED_DAY:
      return state.map(
        workedDay =>
          workedDay.id === action.workedDay.id ? action.workedDay : workedDay
      );
    default:
      return state;
  }
}
