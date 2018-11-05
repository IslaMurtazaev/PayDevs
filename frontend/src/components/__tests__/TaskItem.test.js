import React from "react";
import TaskItem from "../TaskItem";
import { shallow } from "enzyme";
import toJson from "enzyme-to-json";

describe("<TaskItem />", () => {
  it("renders 1 <TaskItem />", () => {
    const task = { title: "Task number 1", description: "Test a ", price: 500 };
    const component = shallow(<TaskItem task={task} />);
    expect(component).toHaveLength(1);
  });

  it("renders attribs <TaskItem />", () => {
    const task = { title: "Task number 1", description: "Test a ", price: 500 };
    const component = shallow(<TaskItem task={task} />);
    expect(component.instance().props.task.title).toBe("Task number 1");
    expect(component.instance().props.task.description).toBe("Test a ");
    expect(component.instance().props.task.price).toBe(500);
  });

  it("renders mount <TaskItem /> h4 count", () => {
    const task = {
      id: 1,
      title: "Task number 1",
      description: "Test a ",
      paid: false,
      price: 500,
      completed: true
    };
    const component = shallow(<TaskItem task={task} />);
    expect(component.find("h4")).toHaveLength(1);
    expect(component.find("h5")).toHaveLength(4);
    expect(component.find(".taskTitle").text()).toBe(`Title: ${task.title}`);
    expect(component.find(".taskDescription").text()).toBe(
      `Description: ${task.description}`
    );
    expect(component.find(".taskPaid").text()).toBe("not paid");
    expect(component.find(".taskPrice").text()).toBe(`Price: ${task.price}`);
    expect(component.find(".taskCompleted").text()).toBe(
      task.completed ? "Completed" : "Uncompleted"
    );
  });

  it("renders mount <TaskItem /> click onDelete", () => {
    const onDeleteSpy = jest.fn();
    const task = {
      id: 1,
      title: "Task number 1",
      description: "Test a ",
      price: 500
    };
    const component = shallow(<TaskItem task={task} onDelete={onDeleteSpy} />);
    component.find(".btn-danger").simulate("click");
    expect(onDeleteSpy).toBeCalledWith(1);
  });

  it("matches previous snapshot", () => {
    const task = {
      id: 1,
      title: "Task number 1",
      description: "Test a ",
      price: 500
    };
    expect(toJson(shallow(<TaskItem task={task} />))).toMatchSnapshot();
  });
});
