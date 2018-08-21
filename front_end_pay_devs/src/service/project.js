import axios from "axios";
import { authHeader } from "./helpers";

export const projectService = {
  get,
  get_all,
  remove,
  create,
  update,
  getTotal
};

const BASE_URL = "http://127.0.0.1:8000/api/project/";

function get(projectId) {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${BASE_URL}${projectId}/`,
    headers: headers
  }).then(res => {
    let project = res.data;
    return project;
  });
}

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

function remove(id) {
  let headers = authHeader();
  return axios({
    method: "delete",
    url: `${BASE_URL}${id}/delete`,
    headers: headers
  }).then(res => {
    let project = res.data;
    return project;
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
  }).then(res => {
    let project = res.data;
    return project;
  });
}

function update(project) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${project.id}/update/`;
  return axios({
    method: "put",
    url: fetch_url,
    headers: headres,
    data: project
  }).then(res => {
    let project = res.data;
    return project;
  });
}

function getTotal(id) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${id}/total`;
  return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: { paid: false }
  }).then(res => {
    return res.data;
  });
}
