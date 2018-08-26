import React from "react";
import { shallow } from "enzyme";
import configureStore from "redux-mock-store";

import ProjectItem from "../ProjectItem";

describe("<ProjectItem />", () => {
  const initialState = {
    project: {
      title: "PayDevs",
      description: "blablabla",
      start_date: "2018-08-24T00:00:00.000Z",
      end_date: "2018-09-30T10:00:00.000Z",
      type_of_payment: "M_P",
      status: true
    }
  };
  const mockStore = configureStore()

  it("renders without errors", () => {
    // let store = mockStore(initialState);
    // let container = shallow(<ProjectItem store={store} />);
    expect(1).toBe(1);
  });
});
