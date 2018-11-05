import axios from "axios";

export const taskService = {
  create,
  getAll,
  remove,
  update
};

const BASE_URL = "/api/project/";

function create(task, projectId) {
  const fetch_url = `${BASE_URL}${projectId}/task/create`;
  return axios.post(fetch_url, task).then(res => {
    return res.data;
  });
}

function getAll(projectId) {
  return axios
    .get(`${BASE_URL}${projectId}/task/all`)
    .then(res => {
      let tasks = res.data;
      return tasks;
    });
}

function remove(taskId) {
  return axios
    .delete(`${BASE_URL}task/${taskId}/delete`)
    .then(res => {
      let task = res.data;
      return task;
    });
}

function update(values) {
  const fetch_url = `${BASE_URL}${values.projectId}/task/${values.id}/update`;
  return axios.put(fetch_url, values).then(res => {
    let task = res.data;
    return task;
  });
}
