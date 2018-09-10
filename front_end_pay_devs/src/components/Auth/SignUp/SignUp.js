import { connect } from "react-redux";
import { userActions } from "../../../actions/user";

import SignUpScreen from "./SignUpScreen";

export default connect(
  state => ({
    user: state.user,
    error: state.user.error
  }),
  dispatch => ({
    onSignUpUser: (username, email, password) => {
      dispatch(userActions.sign_up(username, email, password));
    }
  })
)(SignUpScreen);
