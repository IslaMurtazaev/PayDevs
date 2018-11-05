import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
jest.mock("../../../index.js", () => require("history"));

import ProjectPage from "../ProjectPage";

describe("<ProjectPage />", () => {
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

  let component = shallow(
    <ProjectPage
      user={initialState.user}
      projects={initialState.projects}
      getAllProjects={() => []}
    />
  );
  
  it("calls getAllProjects automatically", () => {
    let getAllProjectsSpy = jest.fn().mockReturnValue([]);

    component = shallow(
      <ProjectPage
        user={initialState.user}
        projects={initialState.projects}
        getAllProjects={getAllProjectsSpy}
      />
    );

    expect(getAllProjectsSpy).toBeCalledTimes(1);
  });

  it("renders projects based on props", () => {
    expect(component.find(".projectInfo")).toHaveLength(2);
  })

  it("renders userInfo based on props", () => {
    expect(component.find(".username").text()).toBe("IslaMurtazaev");
    expect(component.find(".email").text()).toBe("islam.muratazaev@gmail.com");
  });

  it("matches previous snap", () => {
    expect(toJson(component)).toMatchSnapshot();
  });
});
