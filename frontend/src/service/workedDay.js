import axios from "axios";
import { authHeader } from "./helpers"

const API_URL = "/api/";

export default {
  create,
  getAll,
  remove,
  update
};

function create(projectId, monthPaymentId, values) {
  const fetch_url = `${API_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/create`;
  return axios.post(fetch_url, values, { headers: authHeader() }).then(res => {
    let workedDay = res.data;
    return workedDay;
  });
}

function getAll(monthPaymentId) {
  return axios
    .get(`${API_URL}project/month_payment/${monthPaymentId}/worked_day/all`, {
      headers: authHeader()
    })
    .then(res => {
      let workedDays = res.data;
      return workedDays;
    });
}

function remove(workedDayId) {
  return axios
    .delete(`${API_URL}project/worked_day/${workedDayId}/delete`, {
      headers: authHeader()
    })
    .then(res => res.data);
}

function update(projectId, monthPaymentId, workedDayId, values) {
  const fetch_url = `${API_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/${workedDayId}/update`;
  return axios.put(fetch_url, values, { headers: authHeader() }).then(res => {
    let updatedWorkedDay = res.data;
    return updatedWorkedDay;
  });
}
