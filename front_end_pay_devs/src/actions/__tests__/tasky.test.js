import {tasklyActions} from "../task";
import {taskActionTypes} from "../../constants/task"

import {taskService} from "service/task"
jest.mock("../../service/task", () => require('service/task'))
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
jest.mock("../../index", () => require("history"))
jest.mock("../../service/helpers", () => require("helpers"))


const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);


describe('actions Task', () => {
    it('should getAll an action to add a todo', async () => {
      const expectedAction  = {
        type: taskActionTypes.ADD_ALL, tasks: ["task"]
      }
      taskService.getAll.mockImplementationOnce((projectId) =>{
        
          return Promise.resolve(
            ["task"] 
        )
      })
      const store = mockStore({})
       
      return store.dispatch(tasklyActions.getAll(1)).then(() => {
        const action = store.getActions()
        expect(action.length).toBe(1)
        expect(action).toContainEqual(expectedAction)
        expect(taskService.getAll).toHaveBeenCalledTimes(1); 
        
      })
       
    });

    it('should create an action to add a todo', async () => {
      
      const task =  {   
        id: 1,
        title: 'Task one',
        description: 'Task one description',
        price: 1000,
        paid: false,
        completed: true,
        projectId: 1 
    }

      const expectedAction  = {
        type: taskActionTypes.CREATE, task: task
      }
      taskService.create.mockImplementationOnce((task, projectId) =>{
          return Promise.resolve(
            task 
        )
      })
      const store = mockStore({})
       
      return store.dispatch(tasklyActions.create(task, task.projectId)).then(() => {
        const action = store.getActions()
        expect(action.length).toBe(1)
        expect(action.pop()).toEqual(expectedAction)
        expect(taskService.create).toHaveBeenCalledTimes(1); 
        
      })
       
    });


    it('should update an action to add a todo', async () => {
      
      const task =  {   
        id: 1,
        title: 'Task one',
        description: 'Task one description',
        price: 1000,
        paid: false,
        completed: true,
        projectId: 1 
    }

      const expectedAction  = {
        type: taskActionTypes.UPDATE, task: task
      }
      taskService.update.mockImplementationOnce((task) =>{
        
          return Promise.resolve(
            task 
        )
      })
      const store = mockStore({})
       
      return store.dispatch(tasklyActions.update(task)).then(() => {
        const action = store.getActions()
        expect(action.length).toBe(1)
        expect(action.pop()).toEqual(expectedAction)
        expect(taskService.create).toHaveBeenCalledTimes(1); 
      })
       
    });


    it('should remove an action to add a todo', async () => {
      
      const taskId = 1;

      const expectedAction  = {
        type: taskActionTypes.REMOVE, taskId
      }
      taskService.remove.mockImplementationOnce((taskId) =>{
        
          return Promise.resolve(
            taskId
        )
      })
      const store = mockStore({})
       
      return store.dispatch(tasklyActions.remove(taskId)).then(() => {
        const action = store.getActions()
        expect(action.length).toBe(1)
        expect(action.pop()).toEqual(expectedAction)
        expect(taskService.remove).toHaveBeenCalledTimes(1); 
      })
       
    });
  });
