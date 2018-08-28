import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import configureStore from "redux-mock-store";

import HourlyRates from "../HourlyRates";

describe("<HourlyRates />", () => {
  const initialState = {
    hourPayments: [
      { id: 1, rate: 15 },
      { id: 2, rate: 20 },
      { id: 3, rate: 22 }
    ]
  };

  const mockStore = configureStore();
  const store = mockStore(initialState)

  const container = shallow(<HourlyRates store={store} />).dive()

  it("renders rateHeader if there are props.hourPayments", () => {
    expect(container.find(".rateHeader").text()).toBe("Select one of your current rates:");
  });
 
  it("matches previous snapshot", () => {
    expect(toJson(container)).toMatchSnapshot();
  })
});
