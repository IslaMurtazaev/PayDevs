import React from "react";
import { shallow } from "enzyme";
import configureStore from "redux-mock-store";
import toJson from "enzyme-to-json"
jest.mock("../../../index.js", () => require("history"));

import ProjectPage from "../ProjectPage";

describe("<ProjectItem />", () => {
  const initialState = {
    user: {
      user: {
        username: "IslaMurtazaev",
        email: "islam.muratazaev@gmail.com"
      }
    },
    projects: [
      {
        id: 1,
        title: "PayDevs",
        description: "blablabla",
        start_date: "2018-08-24T00:00:00.000Z",
        end_date: "2018-09-30T10:00:00.000Z",
        type_of_payment: "M_P",
        status: true
      },
      {
        id: 2,
        title: "PayDevs2",
        description: "blablabla2",
        start_date: "2018-08-24T00:00:00.000Z",
        end_date: "2018-09-30T10:00:00.000Z",
        type_of_payment: "H_P",
        status: false
      }
    ]
  };
  const mockStore = configureStore();

  let store = mockStore(initialState);
  let container = shallow(<ProjectPage store={store} />).dive();

  it("renders username based on props", () => {
    expect(container.find(".username").text()).toBe("IslaMurtazaev");
  });

  it("renders email based on props", () => {
    expect(container.find(".email").text()).toBe("islam.muratazaev@gmail.com");
  });

  it("matches previous snap", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
