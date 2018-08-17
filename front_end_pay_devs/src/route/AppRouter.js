import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import LoginUser from "../components/Auth/LoginUser";
import ProjectPage from "../components/Project/ProjectPage";
import SignUp from "../components/Auth/SignUp";
import ProjectItem from "../components/Project/ProjectItem";
import { PrivateRoute } from "./PrivateRoute";

import { history } from "../index";
import CreateProjectForm from "../components/Project/CreateProjectForm";
import UpdateProjectForm from "../components/Project/UpdateProjectForm";
import CreateTasklyForm from "../components/Task/CreateTaskly";
import CreateMonthPaymentForm from "../components/MonthPayment/CreateMonthPaymentForm";
import NotFound from "../components/NotFound";
import UpdateTaskForm from "../components/Task/UpdateTaskForm"

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
