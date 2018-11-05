import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
import configureStore from "redux-mock-store";

import MonthlyRates from "../MonthlyRates";

describe("<MonthlyRates />", () => {
  const initialState = {
    monthPayments: [
      { id: 1, rate: 150 },
      { id: 2, rate: 200 },
      { id: 3, rate: 220 }
    ]
  };

  const mockStore = configureStore();
  const store = mockStore(initialState);

  let container;
  beforeEach(() => {
    container = shallow(<MonthlyRates store={store} />).dive();
  });

  it("renders rateHeader if there are props.monthPayments", () => {
    expect(container.find(".rateHeader").text()).toBe(
      "Select one of your current rates:"
    );
  });

  it("matches previous snapshot", () => {
    expect(toJson(container)).toMatchSnapshot();
  });
});
