import React, {Component} from 'react';
import {Router, Route } from 'react-router-dom';

import LoginUser from '../components/LoginUser'
import ProjectPage from '../components/ProjectPage';
import SignUp from '../components/SignUp'
import App from '../App';

import {PrivateRoute} from '../route/PrivateRoute'

import {history} from '../index'


class AppRouter extends Component {

  render() {
    return (
        <Router history={history}>
            <div>
                <Route exact path='/' component={App}/>
                <Route path='/login' component={LoginUser}/>
                <Route path='/sign_up' component={SignUp}/>
                <PrivateRoute path='/projects' component={ProjectPage}/>
            </div>
        </Router>
      
    )
  }
}

export default AppRouter

