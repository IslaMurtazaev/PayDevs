import React, { Component } from "react";
import { connect } from "react-redux";
import { userActions } from "../actions/user";
import { Link } from "react-router-dom";
import logo from './favicon.png';

class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e) {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  }

  handleSubmit(e) {
    e.preventDefault();

    this.setState({ submitted: true });
    const { username, email, password } = this.state;
    if (username && email && password) {
      this.props.onSignUpUser(username, email, password);
      this.setState({ username: "", email: "", password: "" });
    }
  }

  
  render() {
    const { username, password, email } = this.state;
    const error = this.props.error;
    return (
      <div>
        <h2>Sign Up</h2>
        <div className="signUpForm">
        <form name="form" onSubmit={this.handleSubmit}>
          {error && <div>{error.error.message}</div>}
          <div>
            <label htmlFor="username">Username: </label>
            <input
              type="text"
              className="form-control"
              name="username"
              value={username}
              onChange={this.handleChange}
            />
          </div>
          <div>
            <label htmlFor="email">Email: </label>
            <input
              type="email"
              className="form-control"
              name="email"
              value={email}
              onChange={this.handleChange}
            />
          </div>
          <div>
            <label htmlFor="password">Password: </label>
            <input
              type="password"
              className="form-control"
              name="password"
              value={password}
              onChange={this.handleChange}
            />
           </div>
          <div className="form-group">
            <button className="btn btn-primary">Sign Up</button>

            </div>
          </form>
        </div> 
        <div className="loginLink">
        <img src={logo} />          
        <span className="projectName">PayDevs</span>
          <span>Already have an account? </span>
          <Link className="link" to="login">Login</Link>
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
    onSignUpUser: (username, email, password) => {
      dispatch(userActions.sign_up(username, email, password));
    }
  })
)(SignUp);
