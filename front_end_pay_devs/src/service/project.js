import axios from 'axios'
import { authHeader } from './helpers';

export const projectService = {
    get_all,
    
}

function get_all(){
    let headers = authHeader();
    return axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/api/project/all',
        headers: headers
    }).then(res=>{
        let projects = res.data
        return projects
    })
}