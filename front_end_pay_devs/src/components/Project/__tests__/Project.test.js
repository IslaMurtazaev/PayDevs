import React from "react";
import { shallow } from "enzyme";
import configureStore from "redux-mock-store";
import toJson from "enzyme-to-json";
jest.mock("../../../index.js", () => require("history"));

import Project from "../Project";

describe("<Project />", () => {
  const initialState = {
    project: {
      id: 1,
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: true
    }
  };
  const mockStore = configureStore();

  let store = mockStore(initialState);
  let container = shallow(<Project store={store} match={ {params: {id: 1}} } />).dive();

  it("renders projectTitle based on props", () => {
    expect(container.find(".projectTitle").text()).toBe("PayDevs");
  });

  it("renders projectDescription based on props", () => {
    expect(container.find(".projectDescription").text()).toBe(
      "Description: blablabla"
    );
  });

  it("renders projectStartDate based on props", () => {
    expect(container.find(".projectStartDate").text()).toBe(
      "Start date: Fri Aug 24 2018"
    );
  });

  it("renders projectEndDate based on props", () => {
    expect(container.find(".projectEndDate").text()).toBe(
      "End date: Sun Sep 30 2018"
    );
  });

  it("renders projectTypeOfPayment based on props", () => {
    expect(container.find(".projectTypeOfPayment").text()).toBe(
      "Type of payment: Monthly"
    );
  });

  it("renders projectStatus based on props", () => {
    expect(container.find(".projectStatus").text()).toBe("Status: active");
  });

  it("renders three buttons", () => {
    expect(container.find("button")).toHaveLength(3);
  })

  // it("dispatches right action on .removeProject", () => {
  //   container.find(".removeProject").simulate("click");
  //   const actions = store.getActions();
  //   expect(actions).toEqual([ { type: 'REMOVE_PROJECT', projectId: 1 } ]);
  // })
  // it("renders buttons and connects then correctly", () => {
  //   const removeProjectSpy = jest.fn();
  //   container = shallow(<ProjectItem store={store} removeProject={removeProjectSpy} />).dive();
  //   container.find(".removeProject").simulate("click");
  //   expect(removeProjectSpy).toBeCalledWith(1);
  // })

  it("matches previous snap", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
