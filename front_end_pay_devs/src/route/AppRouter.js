import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import LoginUser from "../components/LoginUser";
import ProjectPage from "../components/ProjectPage";
import SignUp from "../components/SignUp";
import ProjectItem from "../components/ProjectItem";
import { PrivateRoute } from "../route/PrivateRoute";

import { history } from "../index";
import CreateProjectForm from "../components/CreateProjectForm";
import CreateTasklyForm from "../components/CreateTaskly"

class AppRouter extends Component {
  render() {
    return (
      <Router history={history}>
        <Switch>
          <PrivateRoute exact path="/" component={ProjectPage} />
          <Route path="/login" component={LoginUser} />
          <Route path="/sign_up" component={SignUp} />
          <PrivateRoute path="/project/create" component={CreateProjectForm} />
          <PrivateRoute path="/project/:id/Taskly/create" component={CreateTasklyForm}/>
          <PrivateRoute path="/project/:id/update" component={UpdateProjectForm} />
          <PrivateRoute path="/project/:id" component={ProjectItem} />
         
        </Switch>
      </Router>
    );
  }
}

export default AppRouter;
