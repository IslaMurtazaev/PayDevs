import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import configureStore from "redux-mock-store";
jest.mock("../../../index.js", () => require("history"));

import WorkTimes from "../WorkTimes";

describe("<WorkTimes />", () => {
  const initialState = {
    workTimes: [
      { id: 1, start_date: "1999-08-24T00:00:00.000Z", end_date: "1999-09-24T00:00:00.000Z", paid: true },
      { id: 2, start_date: "2018-08-30T10:00:00.000Z", end_date: "2018-09-24T00:00:00.000Z", paid: false }
    ]
  };

  const mockStore = configureStore();
  const store = mockStore(initialState)
  const match = {params: {id: 1, hourPaymentId: 1}}

  const container = shallow(<WorkTimes store={store} match={match} />).dive()

  it("renders workedHoursHeader if there are props.workTimes", () => {
    expect(container.find(".workedHoursHeader").text()).toBe("Your Worked Hours");
  });
 
  it("matches previous snapshot", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
