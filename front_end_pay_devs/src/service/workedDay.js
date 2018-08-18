import axios from "axios";

import { authHeader } from "./helpers";
import { API_URL } from "../constants/host";

export default {
  create,
  getAll,
  remove
};

function create(projectId, monthPaymentId, values) {
  const headres = authHeader();
  const fetch_url = `${API_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/create/`;
  return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: values
  }).then(res => {
    return res.data;
  });
}

function getAll(monthPaymentId) {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${API_URL}project/month_payment/${monthPaymentId}/worked_day/all/`,
    headers: headers
  }).then(res => {
    let workedDays = res.data;
    return workedDays;
  });
}

function remove(workedDayID) {
  let headers = authHeader();
  return axios({
    method: "delete",
    url: `${API_URL}project/worked_day${workedDayID}/delete/`,
    headers: headers,
  })
}
