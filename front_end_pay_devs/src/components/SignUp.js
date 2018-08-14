import React, { Component } from 'react';
import {connect} from 'react-redux';
import {userActions} from '../actions/user';
import {Link} from 'react-router';
import {history} from '../index';
class SignUp extends Component {
    constructor(props){
        super(props);
        this.state = {
            username: '',
            email: '',
            password: ''
        }

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
        console.log(username, email, password)
        if(username && email && password){
            this.props.onSignUpUser(username, email, password)
            this.setState({username: '', email: '', password: ''})
            history.push('projects')
        }

        
    }


    render() {
        const { username, password, email } = this.state;
        console.log(this.props.user)
        return (
        <div>   
            <Link to="login">Login</Link>
            <form name="form" onSubmit={this.handleSubmit}>
                    <div >
                        <label htmlFor="username">Username: </label>
                        <input type="text" className="form-control" name="username" value={username} onChange={this.handleChange} />
                    </div>
                    <div >
                        <label htmlFor="email">Email: </label>
                        <input type="email" className="form-control" name="email" value={email} onChange={this.handleChange} />
                    </div>
                    <div >
                        <label htmlFor="password">Password: </label>
                        <input type="password" className="form-control" name="password" value={password} onChange={this.handleChange} />
                    </div>
                    <div className="form-group">
                        <button className="btn btn-primary">Sign Up</button>
                    </div>
                </form>
        </div>
        );
    }
}

export default connect(
    (state) => ({
      user: state.user,
    }),
    dispatch => ({
        onSignUpUser:(username, email, password) => {
            dispatch(userActions.sign_up(username, email, password))
        }
    })
)(SignUp);
