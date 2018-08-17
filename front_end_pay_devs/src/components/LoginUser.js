import React, { Component } from "react";
import { connect } from "react-redux";
import { userActions } from "../actions/user";
import { Form, Control } from "react-redux-form";
import { Link } from "react-router-dom";
import logo from './favicon.png';


class LoginUser extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user_req: false,
      password_req: false,
      redirectToNewPage: false
    };
    this.props.onLogOutUser();
  }

  handleSubmit(values) {
    if (values.username && values.password) {
      this.props.onLoginUser(values.username, values.password);
      this.setState({ password_req: false, user_req: false });
    } else if (!values.username) {
      this.setState({ user_req: true });
    } else if (!values.password) {
      this.setState({ password_req: true });
    }
  }

  render() {
    const { user_req, password_req } = this.state;
    const error = this.props.error;

    return (
      <div>
        <h2>Login</h2>
        <Form className="loginForm"
          model="login.user_form"
          onSubmit={val => this.handleSubmit(val)}
          name="myForm"
        >
          {error && <div> error: {error.error.message}</div>}
          <div>
            <label>Username</label><br/>
            <Control.text model="login.user_form.username" />
            {user_req && <div className="help-block">Username is required</div>}
          </div>
          <div>
            <label>Password</label><br/>
            <Control.password model="login.user_form.password" /><br/>
            {password_req && (
              <div className="help-block">Username is required</div>
            )}
            <button className="btn btn-primary">Login</button>
          </div>
        </Form>
        <div className="signUpLink">
        <img src={logo} />          
        <span className="projectName">PayDevs</span>
          <span className="join"> Join us </span>
          <Link className="link" to="sign_up">Sign Up</Link>
        </div>      
        </div>
    );
  }
}

export default connect(
  state => ({
    user: state.user,
    error: state.user.error
  }),
  dispatch => ({
    onLoginUser: (username, password) => {
      dispatch(userActions.authentication(username, password));
    },
    onLogOutUser: () => {
      dispatch(userActions.logout());
    }
  })
)(LoginUser);
