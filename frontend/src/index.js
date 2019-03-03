import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';
import React from "react";
import ReactDOM from "react-dom";
import "./assets/App.css";

import registerServiceWorker from "./registerServiceWorker";
import { createStore, applyMiddleware } from "redux";
import { Provider } from "react-redux";

import { composeWithDevTools } from "redux-devtools-extension";
import thunk from "redux-thunk";
import reducer from "./reducer";
import { createBrowserHistory } from "history";

import AppRouter from "./route/AppRouter";
import axios from "axios";
import { authHeader } from "./service/helpers";

axios.defaults.headers = authHeader();

const store = createStore(reducer, composeWithDevTools(applyMiddleware(thunk)));

export const history = createBrowserHistory();

ReactDOM.render(
  <Provider store={store}>
    <AppRouter />
  </Provider>,
  document.getElementById("root")
);
registerServiceWorker();
