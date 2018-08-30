import configureMockStore from "redux-mock-store";
import thunk from "redux-thunk";
jest.mock("react-file-download");
import FileDownload from "react-file-download";

import { projectActions } from "../../actions/project";
import { projectActionTypes } from "../../constants/project";
import { projectService } from "../../service/project";
jest.mock("../../service/project.js");

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);
const store = mockStore({ projects: [] });

describe("project's action creators", () => {
  afterEach(() => {
    store.clearActions();
  });

  it("creates GET_ALL_PROJECTS action after fetching projects has been done", () => {
    const fetchedProjects = [
      {
        id: 1,
        title: "PayDevs",
        description: "blablabla",
        start_date: "2018-08-24T00:00:00.000Z",
        end_date: "2018-09-30T10:00:00.000Z",
        type_of_payment: "M_P",
        status: false
      },
      {
        id: 2,
        title: "PayDevs2",
        description: "blablabla2",
        start_date: "2019-08-24T00:00:00.000Z",
        end_date: "2019-09-30T10:00:00.000Z",
        type_of_payment: "H_P",
        status: true
      }
    ];

    projectService.getAll.mockReturnValue(Promise.resolve(fetchedProjects));

    const expectedActions = [
      { type: projectActionTypes.ADD_ALL, projects: fetchedProjects }
    ];

    return store.dispatch(projectActions.getAll()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.getAll).toHaveBeenCalled();
    });
  });

  it("creates CLEAR_ALL_PROJECTS action after clearing projects has been done", () => {
    const expectedActions = [{ type: projectActionTypes.CLEAR_ALL }];

    store.dispatch(projectActions.clearAll());

    expect(store.getActions()).toEqual(expectedActions);
  });

  it("creates GET_PROJECT action after fetching project has been done", () => {
    const fetchedProject = {
      id: 1,
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: false
    };

    projectService.get.mockReturnValue(Promise.resolve(fetchedProject));

    const expectedActions = [
      { type: projectActionTypes.GET, project: fetchedProject }
    ];

    return store.dispatch(projectActions.get()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.get).toHaveBeenCalled();
    });
  });

  it("creates CREATE_PROJECT action after creating new project", () => {
    const createdProject = {
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: false
    };

    projectService.create.mockReturnValue(Promise.resolve(createdProject));

    const expectedActions = [
      { type: projectActionTypes.CREATE, project: createdProject }
    ];

    return store.dispatch(projectActions.create()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.create).toHaveBeenCalled();
    });
  });

  it("creates REMOVE_PROJECT action after removing project", () => {
    const removedProjectId = 1;

    projectService.remove.mockReturnValue(Promise.resolve());

    const expectedActions = [
      { type: projectActionTypes.REMOVE, id: removedProjectId }
    ];

    return store.dispatch(projectActions.remove(removedProjectId)).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.remove).toHaveBeenCalled();
    });
  });

  it("creates UPDATE_PROJECT action after updaing the project", () => {
    const updatedProject = {
      id: 1,
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: false
    };

    projectService.update.mockReturnValue(Promise.resolve(updatedProject));

    const expectedActions = [
      { type: projectActionTypes.UPDATE, project: updatedProject }
    ];

    return store.dispatch(projectActions.update()).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.update).toHaveBeenCalled();
    });
  });

  it("creates GET_TOTAL action after getting total bill of the project", () => {
    const projectId = 1;
    const data = {
      id: 1,
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: true,
      total: 1000
    };

    projectService.getTotal.mockReturnValue(Promise.resolve(data));

    const expectedActions = [{ type: projectActionTypes.GET_TOTAL }];

    return store.dispatch(projectActions.getTotal(projectId)).then(() => {
      expect(store.getActions()).toEqual(expectedActions);
      expect(projectService.getTotal).toHaveBeenCalled();
      expect(FileDownload).toHaveBeenCalled();
      expect(FileDownload).toBeCalledWith(data, "total.pdf");
    });
  });
});
