import axios from "axios";
import { authHeader } from "./helpers"

export const projectService = {
  get,
  getAll,
  remove,
  create,
  update,
  getTotal
};

const BASE_URL = "/api/project/";

function get(projectId) {
  return axios.get(`${BASE_URL}${projectId}`).then(res => {
    let project = res.data;
    return project;
  });
}

function getAll() {
  return axios.get(`${BASE_URL}all`, { headers: authHeader() }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function remove(id) {
  return axios.delete(`${BASE_URL}${id}/delete`, { headers: authHeader() }).then(res => {
    let project = res.data;
    return project;
  });
}

function create(project) {
  const fetch_url = `${BASE_URL}create`;
  return axios.post(fetch_url, project, { headers: authHeader() }).then(res => {
    let project = res.data;
    return project;
  });
}

function update(project) {
  const fetch_url = `${BASE_URL}${project.id}/update`;
  return axios.put(fetch_url, project, { headers: authHeader() }).then(res => {
    let project = res.data;
    return project;
  });
}

function getTotal(id) {
  const fetch_url = `${BASE_URL}${id}/total`;
  return axios.post(fetch_url, { paid: false }, { headers: authHeader() }).then(res => {
    return res.data;
  });
}
