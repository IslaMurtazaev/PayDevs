import React from "react";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";

import WorkedDay from "../WorkedDay";

describe("<WorkedDay />", () => {
  let workedDay;
  let component;
  beforeEach(() => {
    workedDay = {
      id: 1,
      day: "2018-08-24",
      paid: true
    };
    component = shallow(<WorkedDay workedDay={workedDay} />);
  });

  it("renders day based on props.workedDay.date", () => {
    expect(component.find(".date").text()).toBe(
      "Date: 2018-08-24"
    );
  });

  it("renders paid based on props.workedDay.paid", () => {
    expect(component.find(".paid").text()).toBe("paid");
    workedDay.paid = false;
    component = shallow(<WorkedDay workedDay={workedDay} />);
    expect(component.find(".paid").text()).toBe("not paid");
  });

  it("renders remove button based on props.workedDay.onRemove", () => {
    let onRemoveSpy = jest.fn();
    component = shallow(
      <WorkedDay workedDay={workedDay} onRemove={onRemoveSpy} />
    );
    component.find(".btn-danger").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(workedDay.id);
  });

  it("matches previous snapshot", () => {
    expect(toJson(shallow(<WorkedDay workedDay={workedDay} />))).toMatchSnapshot();
  });
});
