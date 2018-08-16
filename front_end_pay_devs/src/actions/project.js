import { projectService } from "../service/project";
import { ProjectConstant } from "../constants/project";
import { history } from "../index";

export const projectActions = {
  getAll,
  clearAll,
  deleteProject,
  create,
  update
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

function deleteProject(id) {
  return dispatch => {
    projectService.deleteProject(id).then(() => {
      dispatch({ type: ProjectConstant.DELETE_PROJECT });
      history.push("/");
    });
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
      .catch(error => {
        alert(error);
      });
  };
}

function update(project) {
  return dispatch => {
    projectService
      .update(project)
      .then(project => {
        dispatch({ type: ProjectConstant.UPDATE_PROJECT, project });
        history.push("/");
      })
      .catch(error => {
        alert(error);
      });
  };
}
