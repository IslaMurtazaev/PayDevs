import axios from "axios";
import { authHeader } from "./helpers";

const BASE_URL = "http://127.0.0.1:8000/api/project/";

export const workTimeService = {
    create,
    getAll,
    deleteWork
};

function create(workTime) {
const headres = authHeader();
const fetch_url = `${BASE_URL}${workTime.projectId}/hour_payment/${workTime.hourPaymentId}/work_time/create`;
return axios({
        method: "post",
        url: fetch_url,
        headers: headres,
        data: workTime
    }).then(res => {
        return res.data;
    });
}


function getAll(hourPaymentId) {
    let headers = authHeader();
    return axios({
      method: "get",
      url: `${BASE_URL}hour_payment/${hourPaymentId}/work_time/all`,
      headers: headers
    }).then(res => {
      let projects = res.data;
      return projects;
    });
  }


  function deleteWork(workId) {
    let headers = authHeader();
    return axios({
      method: "delete",
      url: `${BASE_URL}work_time/${workId}/delete`,
      headers: headers
    }).then(res => {
      let task = res.data;
      return task ;
    });
  }