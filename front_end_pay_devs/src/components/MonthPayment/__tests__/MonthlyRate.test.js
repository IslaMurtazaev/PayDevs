import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";

import MonthlyRate from "../MonthlyRate";

describe("<MonthlyRate />", () => {
  const monthPayment = { id: 1, rate: 150 };

  it("renders rate based on props", () => {
    const component = shallow(<MonthlyRate monthPayment={monthPayment} />);
    expect(component.find(".rate").text()).toBe("150/per day");
  });

  it("renders remove button based on props", () => {
    const onRemoveSpy = jest.fn();
    const component = shallow(<MonthlyRate monthPayment={monthPayment} onRemove={onRemoveSpy} />);
    component.find(".removeRate").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(1);
  });

  it("matches previous snapshot", () => {
    expect(toJson(shallow(<MonthlyRate monthPayment={monthPayment} />))).toMatchSnapshot();
  })
});
