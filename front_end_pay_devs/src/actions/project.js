import { projectService } from "../service/project";
import { ProjectConstant } from "../constants/project";
import { history } from "../index";
import {handleError} from "../service/helpers"


export const projectActions = {
  getAll,
  clearAll,
  remove,
  create,
  update,
  getTotal
};

function getAll() {
  return dispatch => {
    projectService.get_all().then(projects => {
      dispatch({ type: ProjectConstant.ADD_ALL_PROJECTS, projects });
    });
  };
}

function clearAll() {
  return { type: ProjectConstant.CLEAR_ALL_PROJECTS };
}

function remove(id) {
  return dispatch => {
    projectService.remove(id).then(() => {
      dispatch({ type: ProjectConstant.DELETE_PROJECT });
      history.push("/");
    }).catch(error => handleError(error));
  };
}

function create(project) {
  return dispatch => {
    projectService
      .create(project)
      .then(project => {
        dispatch({ type: ProjectConstant.CREATE_PROJECT, project });
        history.push(`/project/${project.id}`);
      })
      .catch(error => handleError(error));
  };
}

function update(project) {
  return dispatch => {
    projectService
      .update(project)
      .then(project => {
        dispatch({ type: ProjectConstant.UPDATE_PROJECT, project });
        history.push(`/project/${project.id}`);
      })
      .catch(error => handleError(error));
  };
}

const FileDownload = require("react-file-download");
function getTotal(id) {
  return dispatch => {
    projectService.getTotal(id).then(data => {
      FileDownload(data, "total.pdf");
      dispatch({ type: ProjectConstant.GET_TOTAL });
      history.push(`/project/${id}`);
    });
  };
}
