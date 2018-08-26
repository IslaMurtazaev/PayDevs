import { project, projects } from "../../reducer/projects";
import { ProjectConstants } from "../../constants/project";

describe("project reducer", () => {
  it("has a default state", () => {
    const defaultState = {};
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(project(undefined, action)).toEqual(defaultState);
  });

  it("triggers GET_PROJECT", () => {
    const retrievedProject = {
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: true
    };
    const action = {
      type: ProjectConstants.GET_PROJECT,
      project: retrievedProject
    };

    expect(project({}, action)).toBe(retrievedProject);
  });
});

describe("projects reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(projects(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL_PROJECTS", () => {
    const retrievedProjects = [
      { title: "PayDevs" },
      { title: "PayDevs2" },
      { title: "PayDevs3" }
    ];
    const action = {
      type: ProjectConstants.ADD_ALL_PROJECTS,
      projects: retrievedProjects
    };

    let result = projects([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedProjects);
  });

  it("triggers CLEAR_ALL_PROJECTS", () => {
    const state = [
      { title: "PayDevs" },
      { title: "PayDevs2" },
      { title: "PayDevs3" }
    ];
    const action = { type: ProjectConstants.CLEAR_ALL_PROJECTS };

    let result = projects(state, action);
    expect(result).toEqual([]);
  });

  it("triggers CREATE_PROJECT", () => {
    const state = [
      { title: "PayDevs" },
      { title: "PayDevs2" },
      { title: "PayDevs3" }
    ];
    const createdProject = { title: "PayDevs4" };
    const action = {
      type: ProjectConstants.CREATE_PROJECT,
      project: createdProject
    };

    let result = projects(state, action);
    expect(result).toEqual([
      { title: "PayDevs" },
      { title: "PayDevs2" },
      { title: "PayDevs3" },
      { title: "PayDevs4" }
    ]);
  });

  it("triggers UPDATE_PROJECT", () => {
    const state = [
      { id: 1, title: "PayDevs", description: "1st project" },
      { id: 2, title: "PayDevs2", description: "second project" },
      { id: 3, title: "PayDevs3", description: "third project" }
    ];
    const updatedProject = {
      id: 1,
      title: "PayDevs1",
      description: "first project"
    };
    const action = {
      type: ProjectConstants.UPDATE_PROJECT,
      project: updatedProject
    };

    let result = projects(state, action);
    expect(result).toEqual([
      { id: 1, title: "PayDevs1", description: "first project" },
      { id: 2, title: "PayDevs2", description: "second project" },
      { id: 3, title: "PayDevs3", description: "third project" }
    ]);
  });
});
