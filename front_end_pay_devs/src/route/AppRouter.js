import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import LoginUser from "../components/LoginUser";
import ProjectPage from "../components/ProjectPage";
import SignUp from "../components/SignUp";
import ProjectItem from "../components/ProjectItem";
import { PrivateRoute } from "./PrivateRoute";

import { history } from "../index";
import CreateProjectForm from "../components/CreateProjectForm";
import UpdateProjectForm from "../components/UpdateProjectForm";
import CreateTasklyForm from "../components/CreateTaskly";
import CreateMonthPaymentForm from "../components/CreateMonthPaymentForm";
import NotFound from "../components/NotFound";
import UpdateTaskForm from "../components/UpdateTaskForm"

class AppRouter extends Component {
  render() {
    return (
      <Router history={history}>
        <Switch>
          <PrivateRoute exact path="/" component={ProjectPage} />
          <Route path="/login" component={LoginUser} />
          <Route path="/sign_up" component={SignUp} />
          <PrivateRoute path="/project/create" component={CreateProjectForm} />
          <PrivateRoute path="/project/:id/Taskly/:taskId/update" component={UpdateTaskForm}/>
          <PrivateRoute path="/project/:id/Taskly/create" component={CreateTasklyForm}/>
          <PrivateRoute path="/project/:id/Monthly/create" component={CreateMonthPaymentForm} />
          <PrivateRoute path="/project/:id/update" component={UpdateProjectForm} />
          <PrivateRoute path="/project/:id" component={ProjectItem} />
          <Route component={NotFound} />
        </Switch>
      </Router>
    );
  }
}

export default AppRouter;
