import mockAxios from "axios"
import {taskService} from '../task'
const fs = require('fs')



const BASE_URL = "/api/"

describe('Task', async () => {
    it('test function getAll', async () => {
        // const a = jest.fn()
        // a.mockImplementationOnce

        let tasks = [ 
            {   id: 1,
                title: 'Task one',
                description: 'Task one description',
                price: 1000,
                paid: false,
                completed: true,
                projectId: 1 
            },
            {   id: 2,
                title: 'Task two',
                description: 'Task two description',
                price: 500,
                paid: false,
                completed: true,
                projectId: 1 
            }
        ]
        
        
        mockAxios.get.mockImplementationOnce(()=>
        new Promise((resolve, reject) => {
            fs.readFile("./src/__mocks__/__mockData__/task.json", 'utf8', (err, data) => {
              if (err) reject(err)
              resolve({ data: JSON.parse(data) })
            })
          })
        )

        const data =  await taskService.getAll(1);
        expect(data).toEqual(tasks);
        expect(mockAxios.get).toHaveBeenCalledTimes(1);
        expect(mockAxios.get).toHaveBeenCalledWith(
            `${BASE_URL}project/1/task/all`
        )
    })

    it('test function Create', async () => {

        const task = { 
            id: 1,
            title: 'Task one',
            description: 'Task one description',
            price: 1000,
            paid: false,
            completed: true,
            projectId: 1 
            }
        
        mockAxios.post.mockImplementationOnce(()=>
        new Promise((resolve, reject) => {
            fs.readFile("./src/__mocks__/__mockData__/task.json", 'utf8', (err, data) => {
              if (err) reject(err)
              
              resolve({ data: JSON.parse(data)[0] })
            })
          })
        )

        const data =  await taskService.create(task, 1);
        
        expect(data).toEqual(task);
        expect(mockAxios.post).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.post).toHaveBeenCalledWith(
            `${BASE_URL}project/1/task/create`,
            {   "id": 1,
                "completed": true,
                "description": "Task one description", 
                "paid": false, 
                "price": 1000, 
                "projectId": 1, 
                "title": "Task one"
            }
            
        )
    });

    it('test function Update', async () => {
        const task = { 
                id: 1,
                title: 'Task one',
                description: 'Task one description',
                price: 1000,
                paid: false,
                completed: true,
                projectId: 1 
            }
        
        mockAxios.put.mockImplementationOnce(()=>
        new Promise((resolve, reject) => {
            
            fs.readFile("./src/__mocks__/__mockData__/task.json", 'utf8', (err, data) => {
              if (err) reject(err)
              
              resolve({ data: JSON.parse(data)[0] })
            })
          })
        )

        const data =  await taskService.update(task);
        expect(data).toEqual(task);
        expect(mockAxios.put).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.put).toHaveBeenCalledWith(
            `${BASE_URL}project/1/task/1/update`,
            {   "id": 1,
                "completed": true,
                "description": "Task one description", 
                "paid": false, 
                "price": 1000, 
                "projectId": 1, 
                "title": "Task one"
            }
            
        )

    });

    it('test function Update', async () => {
        const task = { 
            id: 1,
            title: 'Task one',
            description: 'Task one description',
            price: 1000,
            paid: false,
            completed: true,
            projectId: 1 
            }

        mockAxios.delete.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            
            const urlList = url.split("/")

            urlList.pop()
            const taskId = urlList.pop()
           
            
            fs.readFile("./src/__mocks__/__mockData__/task.json", 'utf8', (err, data) => {
              if (err) reject(err)
              
              resolve({ data: JSON.parse(data).filter(task=>task.id === +taskId).pop() })
            })
          })
        )

        const data =  await taskService.remove(1);
        expect(data).toEqual(task);
        expect(mockAxios.put).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.put).toHaveBeenCalledWith(
            `${BASE_URL}project/1/task/1/update`,
            {   "id": 1,
                "completed": true,
                "description": "Task one description", 
                "paid": false, 
                "price": 1000, 
                "projectId": 1, 
                "title": "Task one"
            }
            
        )
    });

})