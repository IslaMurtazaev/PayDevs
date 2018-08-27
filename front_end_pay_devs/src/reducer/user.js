import { userActionTypes } from "../constants/user";

let user_ = JSON.parse(localStorage.getItem("user"));
const initialState = user_ ? { loggedIn: true, user: user_ } : {};

export default function user(state = initialState, action) {
  switch (action.type) {
    case userActionTypes.LOGIN_USER:
      return { user: action.user };
    case userActionTypes.LOGIN_ERROR:
      return { error: action.error };
  }
  return state;
}
