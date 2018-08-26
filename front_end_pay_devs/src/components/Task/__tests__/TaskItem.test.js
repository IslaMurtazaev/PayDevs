import React from "react";
import TaskItem from "../TaskItem";
import { shallow, mount } from "enzyme";
import ReactRouterEnzymeContext from "react-router-enzyme-context";

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
    const options = new ReactRouterEnzymeContext();
    const task = {
      id: 1,
      title: "Task number 1",
      description: "Test a ",
      paid: false,
      price: 500,
      completed: true
    };
    const component = mount(<TaskItem task={task} />, options.get());
    expect(component.find("h4")).toHaveLength(5);
    expect(component.find(".taskTitle").text()).toBe(`Title: ${task.title}`);
    expect(component.find(".taskDescription").text()).toBe(`Description: ${task.description}`);
    expect(component.find(".taskPaid").text()).toBe("not paid");
    expect(component.find(".taskPrice").text()).toBe(`Price: ${task.price}`);
    expect(component.find(".taskCompleted").text()).toBe(
      task.completed ? "Completed" : "Uncompleted"
    );
    console.log(component.find("Link").text());
  });

  it("renders mount <TaskItem /> click onDelete", () => {
    const onDeleteSpy = jest.fn();
    const options = new ReactRouterEnzymeContext();
    const task = {
      id: 1,
      title: "Task number 1",
      description: "Test a ",
      price: 500
    };
    const component = mount(
      <TaskItem task={task} onDelete={onDeleteSpy} />,
      options.get()
    );
    component.find(".btn-danger").simulate("click");
    expect(onDeleteSpy).toBeCalledWith(1);
  });
});
