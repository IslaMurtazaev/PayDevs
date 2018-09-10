import React, { Component } from "react";
import { Form, Control } from "react-redux-form";
import { Redirect } from "react-router-dom";

class LoginScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user_req: false,
      password_req: false,
      redirectToNewPage: false
    };
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
    if (localStorage.getItem("user")) {
      return <Redirect to="/" from="/login" />;
    }

    const { user_req, password_req } = this.state;
    const error = this.props.error;

    return (
      <div>
        <h2 className="authHeader">Login</h2>
        <Form
          className="loginForm"
          model="login.user_form"
          onSubmit={val => this.handleSubmit(val)}
          name="myForm"
        >
          {error &&
            error.error && (
              <div className="validation-error">{error.error.message}</div>
            )}
          <div>
            <label>Username</label>
            <br />
            <Control.text
              className="usernameInput"
              model="login.user_form.username"
            />
            {user_req && (
              <div className="validation-error">Username is required</div>
            )}
          </div>
          <div>
            <label>Password</label>
            <br />
            <Control.password
              className="passwordInput"
              model="login.user_form.password"
            />
            <br />
            {password_req && (
              <div className="validation-error">Password is required</div>
            )}
            <button className="btn btn-primary">Login</button>
          </div>
        </Form>
      </div>
    );
  }
}

export default LoginScreen;
