import axios from "axios";
import { authHeader } from "./helpers";

export const taskService = {
    create
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