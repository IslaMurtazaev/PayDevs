import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import configureStore from "redux-mock-store";

import Tasks from "../Tasks";

describe("<Tasks />", () => {
  const initialState = {
    tasks: [
      { id: 1, title: "Write Unit Tests", description: "desc1", price: 15, paid: true, completed: true },
      { id: 2, title: "Write Integraion Tests", description: "desc2", price: 20, paid: true, completed: false },
      { id: 3, title: "Write UI Tests", description: "desc3", price: 22, paid: false, completed: true },
      { id: 3, title: "Present the project", description: "desc4", price: 30, paid: false, completed: false }
    ]
  };

  const mockStore = configureStore();
  const store = mockStore(initialState)

  const container = shallow(<Tasks store={store} />).dive()

  it("renders rateHeader if there are props.tasks", () => {
    expect(container.find(".taskHeader").text()).toBe("Your tasks");
  });
 
  it("matches previous snapshot", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
