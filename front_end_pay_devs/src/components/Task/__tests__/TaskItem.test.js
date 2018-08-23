import React from "react";
import TaskItem from "../TaskItem";
import {shallow} from 'enzyme'

describe("<TaskItem />", () =>{
    it("renders 1 <TaskItem />", () =>{
        const task = {title: "Task number 1", description: "Test a ", price: 500}
        const component = shallow(<TaskItem task={task}/>);
        expect(component).toHaveLength(1);
    });
});