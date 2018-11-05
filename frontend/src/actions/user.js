import { UserService } from "../service/user";
import { userActionTypes } from "../constants/user";
import { history } from "../index";

export const userActions = {
  authenticate,
  logout,
  sign_up
};

function authenticate(username, password) {
  return dispatch => 
    UserService.login(username, password).then(
      user => {
        dispatch({ type: userActionTypes.LOGIN_USER, user });
      },
      error => {
        if (error.response)
          dispatch({
            type: userActionTypes.LOGIN_ERROR,
            error: error.response.data
          });
        else dispatch({ type: userActionTypes.LOGIN_ERROR, error: error });
      }
    );
}

function sign_up(username, email, password) {
  return dispatch => 
    UserService.create_user(username, email, password).then(
      user => {
        dispatch({ type: userActionTypes.LOGIN_USER, user });
        history.push("/");
      },
      error => {
        if (error.response)
          dispatch({
            type: userActionTypes.LOGIN_ERROR,
            error: error.response.data
          });
        else dispatch({ type: userActionTypes.LOGIN_ERROR, error: error });
      }
    );
}

function logout() {
  UserService.logout();
  return dispatch => 
    dispatch({ type: userActionTypes.LOGOUT });
}
