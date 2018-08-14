import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';
import {Router, Route,  hashHistory} from 'react-router';
import {syncHistoryWithStore} from 'react-router-redux';
import {composeWithDevTools}  from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import reducer from './reducer';

import LoginUser from './components/LoginUser'
import ProjectPage from './components/ProjectPage';
import SignUp from './components/SignUp'


const store = createStore(reducer, composeWithDevTools((applyMiddleware(thunk))));
export const history = syncHistoryWithStore(hashHistory, store);



ReactDOM.render(
    (<Provider store={store}>
        <Router history={history}>
            <Route path='/' component={App}/>
            <Route path='/login' component={LoginUser}/>
            <Route path='/projects' component={ProjectPage}/>
            <Route path='/sign_up' component={SignUp}/>
        </Router>
    </Provider>),

     document.getElementById('root')
);
registerServiceWorker();
