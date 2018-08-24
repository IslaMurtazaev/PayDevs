import React from "react";
import { shallow } from "enzyme";

import WorkTime from "../WorkTime";

describe("<WorkTime />", () => {
  let workTime;
  beforeEach(() => {
    workTime = {
      id: 1,
      start_work: "2018-08-24T00:00:00.000Z",
      end_work: "2018-09-30T10:00:00.000Z",
      paid: true
    };
  });

  it("renders without errors", () => {
    shallow(<WorkTime workTime={workTime} />);
  });

  it("renders 'Invalid Date' if props.start(end)_work is not valid", () => {
    workTime.start_work = "02-08-1999T00:00:00.000Z";
    workTime.end_work = "05:01:10";
    const workTimeComponent = shallow(<WorkTime workTime={workTime} />);
    expect(workTimeComponent.find(".start_work").text()).toBe(
      "Start Work: Invalid Date"
    );
    expect(workTimeComponent.find(".end_work").text()).toBe(
      "End Work: Invalid Date"
    );
  });

  it("renders start_work based on props", () => {
    const workTimeComponent = shallow(<WorkTime workTime={workTime} />);
    expect(workTimeComponent.find(".start_work").text()).toBe(
      "Start Work: 2018-8-24 06:00:00"
    );
  });

  it("renders end_work based on props", () => {
    const workTimeComponent = shallow(<WorkTime workTime={workTime} />);
    expect(workTimeComponent.find(".end_work").text()).toBe(
      "End Work: 2018-9-30 16:00:00"
    );
  });

  it("renders paid based on props", () => {
    let workTimeComponent = shallow(<WorkTime workTime={workTime} />);
    expect(workTimeComponent.find(".paid").text()).toBe("paid");

    workTime.paid = false;
    workTimeComponent = shallow(<WorkTime workTime={workTime} />);
    expect(workTimeComponent.find(".paid").text()).toBe("not paid");
  });

  it("renders remove button based on props", () => {
    let onRemoveSpy = jest.fn();
    let workTimeComponent = shallow(
      <WorkTime workTime={workTime} onRemove={onRemoveSpy} />
    );
    workTimeComponent.find(".btn-danger").simulate("click");
    expect(onRemoveSpy).toBeCalledWith(workTime.id);
  });
});
