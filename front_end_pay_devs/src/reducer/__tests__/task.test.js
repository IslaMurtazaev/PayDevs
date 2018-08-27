import { task, tasks } from "../task";
import { taskActionTypes } from "../../constants/task";

describe("task reducer", () => {
  it("has a default state", () => {
    const defaultState = {};
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(task(undefined, action)).toEqual(defaultState);
  });

  it("triggers CREATE", () => {
    const createdTask = {
      title: "Finish Unit tests"
    };
    const action = {
      type: taskActionTypes.CREATE,
      task: createdTask
    };

    expect(task({}, action)).toBe(createdTask);
  });
});

describe("tasks reducer", () => {
  it("has a default state", () => {
    const defaultState = [];
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(tasks(undefined, action)).toEqual(defaultState);
  });

  it("triggers ADD_ALL", () => {
    const retrievedTasks = [
      { title: "Finish Unit tests" },
      { title: "Finish Integration tests" },
      { title: "Finish UI tests" }
    ];
    const action = {
      type: taskActionTypes.ADD_ALL,
      tasks: retrievedTasks
    };

    let result = tasks([], action);
    expect(result).toHaveLength(3);
    expect(result).toEqual(retrievedTasks);
  });

  it("triggers REMOVE", () => {
    const state = [
      { id: 1, title: "Finish Unit tests" },
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" }
    ];
    const action = {
      type: taskActionTypes.REMOVE,
      taskId: 1
    };

    let result = tasks(state, action);
    expect(result).toEqual([
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" }
    ]);
  });

  it("triggers CREATE", () => {
    const state = [
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" }
    ];
    const createdTask = { id: 4, title: "Learn how to use Selenium" };
    const action = {
      type: taskActionTypes.CREATE,
      task: createdTask
    };

    let result = tasks(state, action);
    expect(result).toEqual([
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" },
      { id: 4, title: "Learn how to use Selenium" }
    ]);
  });

  it("triggers UPDATE", () => {
    const state = [
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" },
      { id: 4, title: "Learn how to use Selenium" }
    ];
    const updatedTask = {
      id: 4,
      title: "Present PayDevs to Nikita"
    };
    const action = {
      type: taskActionTypes.UPDATE,
      task: updatedTask
    };

    let result = tasks(state, action);
    expect(result).toEqual([
      { id: 2, title: "Finish Integration tests" },
      { id: 3, title: "Finish UI tests" },
      { id: 4, title: "Present PayDevs to Nikita" }
    ]);
  });
});
