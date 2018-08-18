import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";
import { combineForms } from "react-redux-form";

import user from "./user";
import projects from "./projects";
import {task, tasks} from './task';
import monthPayments from "./monthPayments";
import workedDays from "./workedDays";

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
  projects,
  task,
  tasks,
  monthPayments,
  workedDays
});
