import {tasklyActions} from "../task";
// import {taskActionTypes} from "../../constants/task"

import {taskService} from "service/task"
jest.mock("../../service/task", () => require('service/task'))
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';


const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);


describe('actions Task', async () => {
    it('should create an action to add a todo', async () => {

      taskService.getAll.mockImplementationOnce((id) =>{
          return Promise.resolve({
            task: ["task"] 
        })
      })
      const store = mockStore({})
      store.dispatch(tasklyActions.getAll(1))
      expect(taskService.getAll).toHaveBeenCalledTimes(1);
      
      
    });
  });
