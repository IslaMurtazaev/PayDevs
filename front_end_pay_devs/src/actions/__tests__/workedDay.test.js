import workedDayActions from "../workedDay";
import {workedDayActionTypes} from "../../constants/workedDay"

import workedDayService from "service/workedDay"
jest.mock("../../service/workedDay", () => require('service/workedDay'))
import configureMockStore from 'redux-mock-store';
import thunk from 'redux-thunk';
jest.mock("../../index", () => require("history"))
jest.mock("../../service/helpers", () => require("helpers"))


const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);


describe('actions Worked Day', () => {
    it('should getAll an action to add a todo', async () => {
        const projectId = 1;
        const expectedAction  = {
            type: workedDayActionTypes.ADD_ALL, workedDays: ["workedDay"]
          }
          workedDayService.getAll.mockImplementationOnce((projectId) =>{
            
              return Promise.resolve(
                ["workedDay"] 
            )
          })

        const store = mockStore({})

        return store.dispatch(workedDayActions.getAll(projectId)).then(() => {
            const action = store.getActions()
            expect(action.length).toBe(1)
            expect(action).toContainEqual(expectedAction)
            expect(workedDayService.getAll).toHaveBeenCalledTimes(1);   
          })
    });

    it('should create an action to add a todo', async () => {
        const projectId = 1;
        const workedDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        const expectedAction  = {
            type: workedDayActionTypes.CREATE, workedDay
          }
          workedDayService.create.mockImplementationOnce(() =>{
            
              return Promise.resolve(
                workedDay
            )
          })

        const store = mockStore({})

        return store.dispatch(workedDayActions.create(projectId, workedDay.monthPaymentId, workedDay)).then(() => {
            const action = store.getActions()
            expect(action.length).toBe(1)
            expect(action).toContainEqual(expectedAction)
            expect(workedDayService.create).toHaveBeenCalledTimes(1);   
          })
    });

    
    it('should update an action to add a todo', async () => {
        const projectId = 1;
        const workedDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        const expectedAction  = {
            type: workedDayActionTypes.UPDATE, workedDay
          }
          workedDayService.update.mockImplementationOnce(() =>{
            
              return Promise.resolve(
                workedDay
            )
          })

        const store = mockStore({})

        return store.dispatch(workedDayActions.update(projectId, 
            workedDay.monthPaymentId, workedDay.id, workedDay)).then(() => {
            const action = store.getActions()
            expect(action.length).toBe(1)
            expect(action).toContainEqual(expectedAction)
            expect(workedDayService.update).toHaveBeenCalledTimes(1);   
          })
    });

    it('should remove an action to add a todo', async () => {
        const workedDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        const expectedAction  = {
            type: workedDayActionTypes.REMOVE, workedDayId: workedDay.id
          }
          workedDayService.remove.mockImplementationOnce(() =>{
              return Promise.resolve(
                workedDay.id
            )
          })

        const store = mockStore({})

        return store.dispatch(workedDayActions.remove(workedDay.id)).then(() => {
            const action = store.getActions()
            expect(action.length).toBe(1)
            expect(action).toContainEqual(expectedAction)
            expect(workedDayService.remove).toHaveBeenCalledTimes(1);   
          })
    });

});