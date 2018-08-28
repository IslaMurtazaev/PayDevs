// import {tasklyActions} from "../task";
import {taskActionTypes} from "../../constants/task"


describe('actions Task', () => {
    it('should create an action to add a todo', () => {
      const text = 'Finish docs'
      const expectedAction = {
        type: taskActionTypes.CREATE_TASK,
        text
      }
      // expect(tasklyActions.create(1, 2)).toEqual(expectedAction)
    });
  });
