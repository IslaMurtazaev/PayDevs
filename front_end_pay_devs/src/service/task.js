import axios from "axios";
import { authHeader } from "./helpers";

export const taskService = {
  create,
  getAll,
  remove,
  update
};

const BASE_URL = "http://127.0.0.1:8000/api/project/";

function create(task, projectId) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${projectId}/task/create/`;
  return axios.post(fetch_url, task, { headers: headres }).then(res => {
    return res.data;
  });
}

function getAll(projectId) {
  let headers = authHeader();
  return axios
    .get(`${BASE_URL}${projectId}/task/all/`, {
      headers: headers
    })
    .then(res => {
      let tasks = res.data;
      return tasks;
    });
}

function remove(taskId) {
  let headers = authHeader();
  return axios
    .delete(`${BASE_URL}task/${taskId}/delete`, { headers: headers })
    .then(res => {
      let task = res.data;
      return task;
    });
}

function update(values) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${values.projectId}/task/${values.id}/update/`;
  return axios.put(fetch_url, values, { headers: headres }).then(res => {
    let task = res.data;
    return task;
  });
}
