import axios from "axios";
import { authHeader } from "./helpers"

export const taskService = {
  create,
  getAll,
  remove,
  update
};

const BASE_URL = "/api/project/";

function create(task, projectId) {
  const fetch_url = `${BASE_URL}${projectId}/task/create`;
  return axios.post(fetch_url, task, { headers: authHeader() }).then(res => {
    return res.data;
  });
}

function getAll(projectId) {
  return axios
    .get(`${BASE_URL}${projectId}/task/all`, { headers: authHeader() })
    .then(res => {
      let tasks = res.data;
      return tasks;
    });
}

function remove(taskId) {
  return axios
    .delete(`${BASE_URL}task/${taskId}/delete`, { headers: authHeader() })
    .then(res => {
      let task = res.data;
      return task;
    });
}

function update(values) {
  const fetch_url = `${BASE_URL}${values.projectId}/task/${values.id}/update`;
  return axios.put(fetch_url, values, { headers: authHeader() }).then(res => {
    let task = res.data;
    return task;
  });
}
