import axios from "axios";
import { authHeader } from "./helpers"

export default {
  getAll,
  create,
  remove
};

const BASE_URL = "/api/project/";

function getAll(projectId) {
  return axios.get(`${BASE_URL}${projectId}/month_payment/all`, { headers: authHeader() }).then(res => {
    let monthPayments = res.data;
    return monthPayments;
  });
}

function create(projectId, values) {
  return axios
    .post(`${BASE_URL}${projectId}/month_payment/create`, values, { headers: authHeader() })
    .then(res => {
      let monthPayment = res.data;
      return monthPayment;
    });
}

function remove(monthPaymentId) {
  return axios
    .delete(`${BASE_URL}month_payment/${monthPaymentId}/delete`, { headers: authHeader() })
    .then(res => res.data);
}
