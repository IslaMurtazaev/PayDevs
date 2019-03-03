import axios from "axios";
import { authHeader } from "./helpers"

const BASE_URL = "/api/project/";

export const hourPaymentService = {
  getAll,
  create,
  remove,
  update
};

function create(hourPayment) {
  const fetch_url = `${BASE_URL}${hourPayment.projectId}/hour_payment/create`;
  return axios
    .post(fetch_url, hourPayment, { headers: authHeader() })
    .then(res => {
      return res.data;
    });
}

function getAll(projectId) {
  return axios
    .get(`${BASE_URL}${projectId}/hour_payment/all`, { headers: authHeader() })
    .then(res => {
      let projects = res.data;
      return projects;
    });
}

function remove(hourId) {
  return axios
    .delete(`${BASE_URL}hour_payment/${hourId}/delete`, {
      headers: authHeader()
    })
    .then(res => {
      let task = res.data;
      return task;
    });
}

function update(values) {
  const fetch_url = `${BASE_URL}${values.projectId}/hour_payment/${
    values.id
  }/update`;
  return axios.put(fetch_url, values, { headers: authHeader() }).then(res => {
    return res.data;
  });
}
