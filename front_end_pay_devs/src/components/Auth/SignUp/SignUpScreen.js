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
    const { username, password, email, submitted } = this.state;
    const error = this.props.error;
    return (
      <div>
        <h2 className="authHeader">Sign Up</h2>
        <div className="signUpForm">
          <form name="form" onSubmit={this.handleSubmit}>
            {error && <div>{error.error.message}</div>}
            <div>
              <label htmlFor="username">Username: </label>
              {submitted && !username && <div className="validation-error">Username is required</div>}
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
              {submitted && !email && <div className="validation-error">Email is required</div>}
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
              {submitted && !password && <div className="validation-error">Password is required</div>}
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
}

export default SignUp;
