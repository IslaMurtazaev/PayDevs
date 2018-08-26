import { UserService } from "../service/user";
import { userConstants } from "../constants/user";
import { history } from "../index";

export const userActions = {
  authentication,
  logout,
  sign_up
};

function authentication(username, password) {
  return dispatch => {
    UserService.login(username, password).then(
      user => {
        dispatch({ type: userConstants.LOGIN_USER, user });
        history.push("/");
      },
      error => {
        if (error.response)
          dispatch({
            type: userConstants.LOGIN_ERROR,
            error: error.response.data
          });
        else dispatch({ type: userConstants.LOGIN_ERROR, error: error });
      }
    );
  };
}

function sign_up(username, email, password) {
  return dispatch => {
    UserService.create_user(username, email, password).then(
      user => {
        dispatch({ type: userConstants.LOGIN_USER, user });
        history.push("/");
      },
      error => {
        if (error.response)
          dispatch({
            type: userConstants.LOGIN_ERROR,
            error: error.response.data
          });
        else dispatch({ type: userConstants.LOGIN_ERROR, error: error });
      }
    );
  };
}

function logout() {
  UserService.logout();
  return dispatch => {
    dispatch({ type: userConstants.LOGOUT });
  };
}
