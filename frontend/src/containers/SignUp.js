import { connect } from "react-redux";
import { userActions } from "../actions/user";

import SignUp from "../components/SignUp";

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
)(SignUp);
