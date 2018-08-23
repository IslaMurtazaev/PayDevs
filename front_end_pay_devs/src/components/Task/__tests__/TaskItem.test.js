import React from "react";
import TaskItem from "../TaskItem";
import {shallow} from 'enzyme'

describe("<TaskItem />", () =>{
    it("renders 1 <TaskItem />", () =>{
        const component = shallow(<TaskItem/>);
        console.log(component.find('button').className)
        // expect(component).toHaveLength(1);
    });
});