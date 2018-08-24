import React from "react";
import { shallow } from "enzyme";

import MonthRate from "../MonthlyRate";

describe("<MonthRate />", () => {
  it("renders rate based on props", () => {
    const monthPayment = { rate: 150, id: 1 };
    const monthRate = shallow(<MonthRate monthPayment={monthPayment} />);
    expect(monthRate.find(".rate").text()).toBe("150/per day");
  });

  it("renders remove button based on props", () => {
    const onRemoveSpy = jest.fn();
    const monthPayment = { rate: 150, id: 1 };
    const monthRate = shallow(<MonthRate monthPayment={monthPayment} onRemove={onRemoveSpy} />);
    monthRate.find(".removeRate").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(1);
  });
});
