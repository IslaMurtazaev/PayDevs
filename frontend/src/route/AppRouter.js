import React, { Component } from "react";
import { Router, Route, Switch } from "react-router-dom";

import Login from "../containers/Login";
import SignUp from "../containers/SignUp";
import ProjectPage from "../containers/ProjectPage";
import ProjectItem from "../containers/Project";
import { PrivateRoute } from "./PrivateRoute";

import { history } from "../index";
import CreateProjectForm from "../components/CreateProjectForm";
import UpdateProjectForm from "../components/UpdateProjectForm";
import NotFound from "../components/NotFound";
import UpdateTaskForm from "../components/UpdateTaskForm";
import UpdateWorkedDayForm from "../components/UpdateWorkedDayForm";
import NavBar from "../components/NavBar";

import WorkedDays from "../containers/WorkedDays";
import UpdateHourlyForm from "../components/UpdateHourlyForm";
import WorkTimes from "../containers/WorkTimes";
import UpdateWorkTimeForm from "../components/UpdateWorkTimeForm";

class AppRouter extends Component {
  render() {
    return (
      <Router history={history}>
        <div>
          <NavBar />
          <Switch>
            <PrivateRoute exact path="/" component={ProjectPage} />
            <Route path="/login" component={Login} />
            <Route path="/sign_up" component={SignUp} />
            <PrivateRoute path="/project/create" component={CreateProjectForm} />
            <PrivateRoute path="/project/:id/Taskly/:taskId/update" component={UpdateTaskForm}/>
            <PrivateRoute path="/project/:id/Monthly/:monthPaymentId/workedDay/:workedDayId/update" component={UpdateWorkedDayForm} />
            <PrivateRoute path="/project/:id/Monthly/:monthPaymentId/workedDay" component={WorkedDays} />
            <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/update" component={UpdateHourlyForm} />
            <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/workTime/:workTimeId/update" component={UpdateWorkTimeForm} />
            <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/workTime" component={WorkTimes} />
            <PrivateRoute path="/project/:id/update" component={UpdateProjectForm} />
            <PrivateRoute path="/project/:id" component={ProjectItem} />
            <Route component={NotFound} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default AppRouter;
