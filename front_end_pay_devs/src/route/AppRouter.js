import React, { Component } from "react";
import { Router, Route } from "react-router-dom";

import LoginUser from "../components/LoginUser";
import ProjectPage from "../components/ProjectPage";
import SignUp from "../components/SignUp";
import ProjectItem from "../components/ProjectItem";

import { PrivateRoute } from "../route/PrivateRoute";

import { history } from "../index";
import CreateProjectForm from "../components/CreateProjectForm";

class AppRouter extends Component {
  render() {
    return (
      <Router history={history}>
        <div>
          <PrivateRoute path="/createproject" component={CreateProjectForm} />
          <PrivateRoute exact path="/" component={ProjectPage} />
          <Route path="/login" component={LoginUser} />
          <Route path="/sign_up" component={SignUp} />
          <PrivateRoute path="/project/:id" component={ProjectItem} />
        </div>
      </Router>
    );
  }
}

export default AppRouter;
