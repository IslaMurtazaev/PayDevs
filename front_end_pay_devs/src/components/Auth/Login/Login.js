import { connect } from "react-redux";
import { userActions } from "../../../actions/user";
import LoginScreen from "./LoginScreen";

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
)(LoginScreen);
