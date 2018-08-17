import { combineReducers } from "redux";
import { routerReducer } from "react-router-redux";
import { combineForms } from "react-redux-form";

import user from "./user";
import project from "./project";
import projects from "./projects";
import {task, tasks} from './task';

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
  tasks
});
