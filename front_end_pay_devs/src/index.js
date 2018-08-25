import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';

import registerServiceWorker from './registerServiceWorker';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';

import {composeWithDevTools}  from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import reducer from './reducer';
import {createBrowserHistory} from 'history'

import AppRouter from './route/AppRouter'



const store = createStore(reducer, composeWithDevTools((applyMiddleware(thunk))));

export const history = createBrowserHistory();


ReactDOM.render(
    (<Provider store={store}>
        <AppRouter/>
    </Provider>),
     document.getElementById('root')
);
registerServiceWorker();
