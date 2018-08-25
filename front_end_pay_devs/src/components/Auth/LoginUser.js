import React, { Component } from "react";
import { connect } from "react-redux";
import { userActions } from "../../actions/user";
import { Form, Control } from "react-redux-form";

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
      console.log(values)
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
         
        <h2 className="authHeader">Login</h2>
        <Form className="loginForm"
          model="login.user_form"
          onSubmit={val => this.handleSubmit(val)}
          name="myForm"
        >
          {error && <div>{error.message}</div>}
          <div>
            <label>Username</label><br/>
            <Control.text className="form-control" model="login.user_form.username" />
            {user_req && <div className="help-block">Username is required</div>}
          </div>
          <div>
            <label>Password</label><br/>
            <Control.password className="form-control" model="login.user_form.password" /><br/>
            {password_req && (
              <div className="help-block">Username is required</div>
            )}
            <button className="submit btn btn-primary">Login</button>
          </div>
        </Form>
     
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
