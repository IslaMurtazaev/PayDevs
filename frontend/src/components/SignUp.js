import React, { Component } from "react";

class SignUp extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      email: "",
      password: "",
      submitted: false
    };
  }

  handleChange = e => {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  };

  handleSubmit = e => {
    e.preventDefault();

    this.setState({ submitted: true });
    const { username, email, password } = this.state;
    if (username && email && password) {
      this.props.onSignUpUser(username, email, password);
    }
  };

  render() {
    const { username, password, email } = this.state;

    return (
      <div>
        <h2 className="authHeader">Sign Up</h2>
        <div className="signUpForm">
          <form name="form" onSubmit={this.handleSubmit}>
            {this.validateForm()}
            <div>
              <label htmlFor="username">Username: </label>
              {this.validateUsername()}
              <input
                type="text"
                className="usernameInput form-control"
                name="username"
                value={username}
                onChange={this.handleChange}
              />
            </div>
            <div>
              <label htmlFor="email">Email: </label>
              {this.validateEmail()}
              <input
                type="email"
                className="emailInput form-control"
                name="email"
                value={email}
                onChange={this.handleChange}
              />
            </div>
            <div>
              <label htmlFor="password">Password: </label>
              {this.validatePassword()}
              <input
                type="password"
                className="passwordInput form-control"
                name="password"
                value={password}
                onChange={this.handleChange}
              />
            </div>
            <button className="btn btn-primary">Sign Up</button>
          </form>
        </div>
      </div>
    );
  }

  validateForm() {
    const submitted = this.state.submitted;
    const error = this.props.error;

    return (
      submitted &&
      error &&
      error.error.message !== "Entity not found" && (
        <div className="validation-error">{error.error.message}</div>
      )
    );
  }

  validateUsername() {
    const { username, submitted } = this.state;

    return (
      submitted &&
      !username && <div className="validation-error">Username is required</div>
    );
  }

  validateEmail() {
    const { email, submitted } = this.state;

    return (
      submitted &&
      !email && <div className="validation-error">Email is required</div>
    );
  }

  validatePassword() {
    const { password, submitted } = this.state;

    return (
      submitted &&
      !password && <div className="validation-error">Password is required</div>
    );
  }
}

export default SignUp;
