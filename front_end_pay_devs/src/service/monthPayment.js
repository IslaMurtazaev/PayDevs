import axios from "axios";
import { authHeader } from "./helpers";

export default {
  getAll, 
  create,
  remove
};

const BASE_URL = "http://127.0.0.1:8000/api/project/";

function getAll(projectId) {
  let headers = authHeader();
  return axios.get( `${BASE_URL}${projectId}/month_payment/all/`,
    {headers: headers}
  ).then(res => {
    let month_payments = res.data;
    return month_payments;
  });
}

function create(projectId, values) {
  let headers = authHeader();
  return axios.post(`${BASE_URL}${projectId}/month_payment/create/`, values,
    {headers: headers}
  ).then(res => {
    let month_payment = res.data;
    return month_payment;
  });
}

function remove(monthPaymentId) {
  let headers = authHeader();
  return axios.delete(
    `${BASE_URL}month_payment/${monthPaymentId}/delete/`,
    {headers: headers},
  )
}
