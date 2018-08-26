import { projectService } from "../service/project";
import { ProjectConstants } from "../constants/project";
import { history } from "../index";
import {handleError} from "../service/helpers"


export const projectActions = {
  get,
  getAll,
  clearAll,
  remove,
  create,
  update,
  getTotal
};

function get(projectId) {
  return dispatch => {
    projectService.get(projectId).then(project => {
      dispatch({ type: ProjectConstants.GET_PROJECT, project });
    });
  };
}

function getAll() {
  return dispatch => {
    projectService.get_all().then(projects => {
      dispatch({ type: ProjectConstants.ADD_ALL_PROJECTS, projects });
    });
  };
}

function clearAll() {
  return { type: ProjectConstants.CLEAR_ALL_PROJECTS };
}

function remove(id) {
  return dispatch => {
    projectService.remove(id).then(() => {
      dispatch({ type: ProjectConstants.DELETE_PROJECT });
      history.push("/");
    }).catch(error => handleError(error));
  };
}

function create(project) {
  return dispatch => {
    projectService
      .create(project)
      .then(project => {
        dispatch({ type: ProjectConstants.CREATE_PROJECT, project });
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
        dispatch({ type: ProjectConstants.UPDATE_PROJECT, project });
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
      dispatch({ type: ProjectConstants.GET_TOTAL });
      history.push(`/project/${id}`);
    });
  };
}
