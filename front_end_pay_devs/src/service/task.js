import axios from "axios";
import { authHeader } from "./helpers";

export const taskService = {
    create,
    getAll,
    remove,
    update
  };


const BASE_URL = "http://127.0.0.1:8000/api/project/";

function create(task, projectId) {
const headres = authHeader();
const fetch_url = `${BASE_URL}${projectId}/task/create/`;
return axios({
    method: "post",
    url: fetch_url,
    headers: headres,
    data: task
}).then(res => {
    return res.data;
});
}


function getAll(projectId) {
  let headers = authHeader();
  return axios({
    method: "get",
    url: `${BASE_URL}${projectId}/task/all/`,
    headers: headers
  }).then(res => {
    let projects = res.data;
    return projects;
  });
}

function remove(taksId) {
    let headers = authHeader();
    return axios({
      method: "delete",
      url: `${BASE_URL}task/${taksId}/delete`,
      headers: headers
    }).then(res => {
      let task = res.data;
      return task ;
    });
  }

  function update(values){
   
    const headres = authHeader();
  const fetch_url = `${BASE_URL}${values.projectId}/task/${values.id}/update/`;
  return axios({
      method: "put",
      url: fetch_url,
      headers: headres,
      data: values
  }).then(res => {
      return res.data;
  });
  }
