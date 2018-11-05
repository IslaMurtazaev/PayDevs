import axios from "axios";

const API_URL = "/api/";

export const workTimeService = {
  create,
  getAll,
  remove,
  update
};

function create(values) {
  const fetch_url = `${API_URL}project/${values.projectId}/hour_payment/${
    values.hourPaymentId
  }/work_time/create`;
  return axios.post(fetch_url, values).then(res => {
    return res.data;
  });
}

function getAll(hourPaymentId) {
  return axios
    .get(`${API_URL}project/hour_payment/${hourPaymentId}/work_time/all`)
    .then(res => {
      let projects = res.data;
      return projects;
    });
}

function remove(workTimeId) {
  return axios
    .delete(`${API_URL}project/work_time/${workTimeId}/delete`)
    .then(res => {
      let task = res.data;
      return task;
    });
}

function update(projectId, hourPaymentId, workTimeId, values) {
  const fetch_url = `${API_URL}project/${projectId}/hour_payment/${hourPaymentId}/work_time/${workTimeId}/update`;
  return axios.put(fetch_url, values).then(res => {
    let updatedWorkTime = res.data;
    return updatedWorkTime;
  });
}
