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
import CreateTaskForm from "../components/Task/CreateTask";
import CreateMonthPaymentForm from "../components/MonthPayment/CreateMonthPaymentForm";
import NotFound from "../components/NotFound";
import UpdateTaskForm from "../components/Task/UpdateTaskForm";
import UpdateWorkedDayForm from "../components/WorkedDay/UpdateWorkedDayForm";
import WorkedDays from "../components/WorkedDay/WorkedDays";
import CreateHourPayment from "../components/HourPayment/CreateHourPayment";
import UpdateHourlyForm from "../components/HourPayment/UpdateHourlyForm";
import WorkTimes from "../components/WorkTime/WorkTimes";
import UpdateWorkTimeForm from "../components/WorkTime/UpdateWorkTimeForm";

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
          <PrivateRoute path="/project/:id/Taskly/create" component={CreateTaskForm}/>
          <PrivateRoute path="/project/:id/Monthly/create" component={CreateMonthPaymentForm} />
          <PrivateRoute path="/project/:id/Monthly/:monthPaymentId/workedDay/:workedDayId/update" component={UpdateWorkedDayForm} />
          <PrivateRoute path="/project/:id/Monthly/:monthPaymentId/workedDay" component={WorkedDays} />
          <PrivateRoute path="/project/:id/Hourly/create" component={CreateHourPayment} />
          <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/update" component={UpdateHourlyForm} />
          <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/workTime/:workTimeId/update" component={UpdateWorkTimeForm} />
          <PrivateRoute path="/project/:id/Hourly/:hourPaymentId/workTime" component={WorkTimes} />
          <PrivateRoute path="/project/:id/update" component={UpdateProjectForm} />
          <PrivateRoute path="/project/:id" component={ProjectItem} />
          <Route component={NotFound} />
        </Switch>
      </Router>
    );
  }
}

export default AppRouter;
