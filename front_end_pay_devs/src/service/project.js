import axios from "axios";

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
  return axios.get(`/api/project/all`).then(res => {
    let projects = res.data;
    return projects;
  });
}

function remove(id) {
  return axios.delete(`/api/project/${id}/delete`).then(res => {
    let project = res.data;
    return project;
  });
}

function create(project) {
  const fetch_url = `/api/project/create`;
  return axios.post(fetch_url, project).then(res => {
    let project = res.data;
    return project;
  });
}

function update(project) {
  const fetch_url = `/api/project/${project.id}/update`;
  return axios.put(fetch_url, project).then(res => {
    let project = res.data;
    return project;
  });
}

function getTotal(id) {
  const fetch_url = `/api/project/${id}/total`;
  return axios.post(fetch_url, { paid: false }).then(res => {
    return res.data;
  });
}
