import axios from "axios";
import { authHeader } from "./helpers";

export const projectService = {
  get_all,
  deleteProject,
  create,
  update
};

const BASE_URL = "http://127.0.0.1:8000/api/project/";

function get_all() {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${BASE_URL}all`,
    headers: headers
  }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function deleteProject(id) {
  let headers = authHeader();
  return axios({
    method: "delete",
    url: `${BASE_URL}${id}/delete`,
    headers: headers
  }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function create(project) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}create`;
  return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: project
  }).then(res => res.data);
}

function update(project) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${project.id}/update/`;
  return axios({
    method: "put",
    url: fetch_url,
    headers: headres,
    data: project
  }).then(res => res.data);
}
