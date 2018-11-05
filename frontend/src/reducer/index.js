import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";
import { combineForms } from "react-redux-form";

import user from "./user";
import { project, projects } from "./projects";
import { task, tasks } from "./task";
import { hourPayment, hourPayments } from "./hourPayment";
import monthPayments from "./monthPayments";
import workedDays from "./workedDays";
import { workTime, workTimes } from "./workTime";

const initialUser = {
  username: "",
  password: ""
};

export default combineReducers({
  login: combineForms(
    {
      user_form: initialUser
    },
    "login"
  ),
  routing: routerReducer,
  user,
  project,
  projects,
  task,
  tasks,
  monthPayments,
  workedDays,
  hourPayment,
  hourPayments,
  workTime,
  workTimes
});
