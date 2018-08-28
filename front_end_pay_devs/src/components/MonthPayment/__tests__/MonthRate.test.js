import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";

import MonthRate from "../MonthlyRate";

describe("<MonthRate />", () => {
  const monthPayment = { rate: 150, id: 1 };

  it("renders rate based on props", () => {
    const monthRate = shallow(<MonthRate monthPayment={monthPayment} />);
    expect(monthRate.find(".rate").text()).toBe("150/per day");
  });

  it("renders remove button based on props", () => {
    const onRemoveSpy = jest.fn();
    const monthRate = shallow(<MonthRate monthPayment={monthPayment} onRemove={onRemoveSpy} />);
    monthRate.find(".removeRate").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(1);
  });

  it("matches previous snapshot", () => {
    expect(toJson(shallow(<MonthRate monthPayment={monthPayment} />))).toMatchSnapshot();
  })
});
