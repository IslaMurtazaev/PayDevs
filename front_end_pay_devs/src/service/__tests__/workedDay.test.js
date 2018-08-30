import mockAxios from "axios"
import workedDayService from '../workedDay'
jest.mock("../helpers", () => require("helpers"))
const fs = require('fs')

const BASE_URL = "http://127.0.0.1:8000/api/"

describe('Worked Day', async () => {
    it('test function getAll', async () => {
        const montPaymentId = 1
        const workDays = [ 
            { 
                id: 1, 
                day: '2018-08-01', 
                paid: false, 
                monthPaymentId: 1 
            },
            { 
                id: 2, 
                day: '2018-08-02', 
                paid: false, 
                monthPaymentId: 1 
            } 
        ]
        mockAxios.get.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            const urlList = url.split("/")
            urlList.pop()
            urlList.pop()
            urlList.pop()
            const monthPaymnetId = urlList.pop()
            
            fs.readFile("./src/__mocks__/__mockData__/workedDay.json", 'utf8', (err, data) => {
              if (err) reject(err)
              resolve({ data: JSON.parse(data).filter(workDay => workDay.monthPaymentId === +monthPaymnetId) })
            })
          })
        )

        const data =  await workedDayService.getAll(montPaymentId);
        expect(data).toEqual(workDays)
        
        expect(mockAxios.get).toHaveBeenCalledTimes(1);
        expect(mockAxios.get).toHaveBeenCalledWith(
            `${BASE_URL}project/month_payment/${montPaymentId}/worked_day/all/`,
            {
                "headers": {}
            }
        )
    });

    it('test function create', async () => {
        const projectId = 1;
        const monthPaymentId = 1;
        const workDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        mockAxios.post.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            fs.readFile("./src/__mocks__/__mockData__/workedDay.json", 'utf8', (err, data) => {
                const urlList = url.split("/")
                urlList.pop()
                urlList.pop()
                urlList.pop()
                const monthPaymnetId = urlList.pop()
                
                if (err) reject(err)
              
                resolve({ data: JSON.parse(data).filter(workDay => workDay.monthPaymentId === +monthPaymnetId ).shift() })
            })
          })
        )

        const data =  await workedDayService.create(projectId, monthPaymentId,  workDay);
        
        expect(data).toEqual(workDay)
        expect(mockAxios.post).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.post).toHaveBeenCalledWith(
            `${BASE_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/create/`,
            { 
                "id": 1, 
                "day": "2018-08-01", 
                "paid": false, 
                "monthPaymentId": 1 
            },
            {"headers": {}}

        )
    });

    it('test function Update', async () => {
        const projectId = 1;
        const monthPaymentId = 1;
        const workDayId = 1;
        const workDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        mockAxios.put.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            
            fs.readFile("./src/__mocks__/__mockData__/workedDay.json", 'utf8', (err, data) => {
              if (err) reject(err)
              const urlList = url.split("/")
                urlList.pop()
                urlList.pop()
                const workDayId = urlList.pop()
                
              resolve({ data: JSON.parse(data).filter(workDay => workDay.id === +workDayId).pop() })
            })
          })
        )

        const data =  await workedDayService.update(projectId, monthPaymentId, workDayId, workDay);
        
        expect(data).toEqual(workDay);
        expect(mockAxios.put).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.put).toHaveBeenCalledWith(
            `${BASE_URL}project/${projectId}/month_payment/${monthPaymentId}/worked_day/${workDayId}/update/`,
            { 
                "id": 1, 
                "day": '2018-08-01', 
                "paid": false, 
                "monthPaymentId": 1 
            },
            {
                "headers": {}
            }
            
        )
    });

    it('test function Remove', async () => {
        
        const workDayId = 1;
        const workDay = { 
            id: 1, 
            day: '2018-08-01', 
            paid: false, 
            monthPaymentId: 1 
        }
        mockAxios.delete.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            
            const urlList = url.split("/")

            urlList.pop()
            urlList.pop()
            const workDayId = urlList.pop()
            
            fs.readFile("./src/__mocks__/__mockData__/workedDay.json", 'utf8', (err, data) => {
              if (err) reject(err)
              
              resolve({ data: JSON.parse(data).filter(workDay => workDay.id === +workDayId).pop()})
            })
          })
        )

        const data =  await workedDayService.remove(workDayId);
        expect(data).toEqual(workDay);
        expect(mockAxios.delete).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.delete).toHaveBeenCalledWith(
            `${BASE_URL}project/worked_day/${workDayId}/delete/`,
            {
                "headers": {}
            }
            
        )
    });
})