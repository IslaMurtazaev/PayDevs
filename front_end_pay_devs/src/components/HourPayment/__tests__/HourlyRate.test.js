import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";
jest.mock("../../../index.js", () => require("history"));

import HourlyRate from "../HourlyRate";

describe("<HourlyRate />", () => {
  const hourPayment = { id: 1, rate: 15 };

  it("renders rate based on props", () => {
    const component = shallow(<HourlyRate hourPayment={hourPayment} />);
    expect(component.find(".rate").text()).toBe("15/per hour");
  });

  it("renders remove button based on props", () => {
    const onRemoveSpy = jest.fn();
    const component = shallow(<HourlyRate hourPayment={hourPayment} onRemove={onRemoveSpy} />);
    component.find(".removeRate").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(1);
  });

  it("matches previous snapshot", () => {
    expect(toJson(shallow(<HourlyRate hourPayment={hourPayment} />))).toMatchSnapshot();
  })
});
