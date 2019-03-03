import { projectService } from "../service/project";
import { projectActionTypes } from "../constants/project";
import { history } from "../index";
import { handleError } from "../service/helpers";

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
  return dispatch =>
    projectService.get(projectId).then(project => {
      dispatch({ type: projectActionTypes.GET, project });
    });
}

function getAll() {
  return dispatch => {
    dispatch({ type: projectActionTypes.GET_ALL });
    projectService
      .getAll()
      .then(projects => {
        dispatch({ type: projectActionTypes.GET_ALL_SUCCESS, projects });
      })
      .catch(errors => {
        dispatch({ type: projectActionTypes.GET_ALL_FAILURE, errors });
      });
  };
}

function clearAll() {
  return { type: projectActionTypes.CLEAR_ALL };
}

function remove(id) {
  return dispatch =>
    projectService
      .remove(id)
      .then(() => {
        dispatch({ type: projectActionTypes.REMOVE, id });
        history.push("/");
      })
      .catch(error => handleError(error));
}

function create(project) {
  return dispatch =>
    projectService
      .create(project)
      .then(project => {
        dispatch({ type: projectActionTypes.CREATE, project });
        history.push(`/project/${project.id}`);
      })
      .catch(error => handleError(error));
}

function update(project) {
  return dispatch =>
    projectService
      .update(project)
      .then(project => {
        dispatch({ type: projectActionTypes.UPDATE, project });
        history.push(`/project/${project.id}`);
      })
      .catch(error => handleError(error));
}

const FileDownload = require("react-file-download");
function getTotal(id) {
  return dispatch =>
    projectService.getTotal(id).then(data => {
      FileDownload(data, "total.pdf");
      dispatch({ type: projectActionTypes.GET_TOTAL });
    });
}
