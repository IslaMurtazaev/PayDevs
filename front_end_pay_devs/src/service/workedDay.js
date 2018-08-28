import axios from "axios";

import { authHeader } from "./helpers";
import { API_URL } from "../constants/host";

export default {
  create,
  getAll,
  remove,
  update
};

function create(projectId, monthPaymentId, values) {
  const headres = authHeader();
  const fetch_url = `${API_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/create/`;
  return axios.post(fetch_url, values,
    {headers: headres},
    
  ).then(res => {
    let workedDay = res.data;
    return workedDay;
  });
}

function getAll(monthPaymentId) {
  let headers = authHeader();
  return axios.get( `${API_URL}project/month_payment/${monthPaymentId}/worked_day/all/`,
    {headers: headers}).then(res => {
    let workedDays = res.data;
    return workedDays;
  });
}

function remove(workedDayId) {
  let headers = authHeader();
  return axios.delete( `${API_URL}project/worked_day/${workedDayId}/delete/`,
    {headers: headers}).then(res => res.data);
}

function update(projectId, monthPaymentId, workedDayId, values) {
  const headres = authHeader();
  const fetch_url = `${API_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/${workedDayId}/update/`;
  return axios.put(fetch_url, values,
    {headers: headres},
    ).then(res => {
    let updatedWorkedDay = res.data;
    return updatedWorkedDay;
  });
}
