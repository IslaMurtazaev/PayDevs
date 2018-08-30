import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import configureStore from "redux-mock-store";
jest.mock("../../../index.js", () => require("history"));

import WorkedDays from "../WorkedDays";

describe("<WorkedDays />", () => {
  const initialState = {
    workedDays: [
      { id: 1, date: "02-08-1999", paid: true },
      { id: 2, date: "02-08-2018", paid: false }
    ]
  };

  const mockStore = configureStore();
  const store = mockStore(initialState)
  const match = {params: {id: 1, monthPaymentId: 1}}

  const container = shallow(<WorkedDays store={store} match={match} />).dive()

  it("renders workedDaysHeader if there are props.workedDays", () => {
    expect(container.find(".workedDaysHeader").text()).toBe("Your Worked Days");
  });
 
  it("matches previous snapshot", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
