import { connect } from "react-redux";
import { userActions } from "../actions/user";
import Login from "../components/Login";

export default connect(
  state => ({
    user: state.user,
    error: state.user.error
  }),
  dispatch => ({
    onLoginUser: (username, password) => {
      dispatch(userActions.authenticate(username, password));
    },
    onLogOutUser: () => {
      dispatch(userActions.logout());
    }
  })
)(Login);
