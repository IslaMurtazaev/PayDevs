import axios from "axios";
import { authHeader } from "./helpers";

const BASE_URL = "http://127.0.0.1:8000/api/project/";

export const hourPaymentService = {
  getAll,
  create,
  remove,
  update
};

function create(hourPayment) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${hourPayment.projectId}/hour_payment/create/`;
  return axios.post( fetch_url, hourPayment,
    {headers: headres}
  ).then(res => {
    return res.data;
  });
}

function getAll(projectId) {
  let headers = authHeader();
  return axios.get(`${BASE_URL}${projectId}/hour_payment/all/`,
    {headers: headers}
  ).then(res => {
    let projects = res.data;
    return projects;
  });
}

function remove(hourId) {
  let headers = authHeader();
  return axios.delete(`${BASE_URL}hour_payment/${hourId}/delete`,
    {headers: headers}
  ).then(res => {
    let task = res.data;
    return task;
  });
}

function update(values) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${values.projectId}/hour_payment/${
    values.id
  }/update/`;
  return axios.put(fetch_url, values,
    {headers: headres},
  ).then(res => {
    return res.data;
  });
}
