import axios from "axios";
import { authHeader } from "./helpers";

export const projectService = {
  get_all,
  deleteProject,
  create,
  getTotal
};

const BASE_URL = "http://127.0.0.1:8000/api/project/";

function get_all() {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${BASE_URL}all`,
    headers: headers
  }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function deleteProject(id) {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${BASE_URL}${id}/delete`,
    headers: headers
  }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function create(project) {
  const headres = authHeader();
  const fetch_url = `${BASE_URL}create`;
  return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: project
  }).then(res => {
    return res.data;
  });
}


function getTotal(id){
  const headres = authHeader();
  const fetch_url = `${BASE_URL}${id}/total`;
  return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: {}
  }).then(res => {
    
    return res.data;
  });
}