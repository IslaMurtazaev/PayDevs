import mockAxios from "axios";
import {hourPaymentService} from '../hourPayment';
const fs = require('fs');

const BASE_URL = "http://127.0.0.1:8000/api/";


describe('Hour Payment', async () => {
    it('test function getAll', async () => {
        const projectId = 1;
        const hourPayments =  [ 
            { id: 1, projectId: 1, rate: 500 },
            { id: 2, projectId: 1, rate: 100 } 
        ]
        mockAxios.get.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            const urlList = url.split("/")
            urlList.pop()
            urlList.pop()
            urlList.pop()
            const projectId = urlList.pop()
            fs.readFile("./src/__mocks__/__mockData__/hourPayment.json", 'utf8', (err, data) => {
              if (err) reject(err)
              resolve({ data: JSON.parse(data).filter(hourPayment => hourPayment.projectId === +projectId) })
            })
          })
        )

        const data =  await hourPaymentService.getAll(projectId);
        expect(data).toEqual(hourPayments) 
        expect(mockAxios.get).toHaveBeenCalledTimes(1);
        expect(mockAxios.get).toHaveBeenCalledWith(
            `${BASE_URL}project/${projectId}/hour_payment/all/`,
            {
                "headers": {}
            }
        )
    });

    it('test function create', async () => {

        const hourPayment = { id: 1, projectId: 1, rate: 500 }
        mockAxios.post.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            fs.readFile("./src/__mocks__/__mockData__/hourPayment.json", 'utf8', (err, data) => {
                const urlList = url.split("/")
                urlList.pop()
                urlList.pop()
                urlList.pop()
                const projectId = urlList.pop()                
                if (err) reject(err)
              
                resolve({ data: JSON.parse(data).filter(hourPayment => 
                    hourPayment.projectId === +projectId ).shift() })
            })
          })
        )

        const data =  await hourPaymentService.create(hourPayment);
        expect(data).toEqual(hourPayment);
        expect(mockAxios.post).toHaveBeenCalledTimes(1);
        expect(mockAxios.post).toHaveBeenCalledWith(
            `${BASE_URL}project/${hourPayment.projectId}/hour_payment/create/`,
            {
                "id": 1,
                "projectId": 1,
                "rate": 500
            },
            {"headers": {}}
        );
    });

    it('test function Update', async () => {

        const hourPayment = { id: 1, projectId: 1, rate: 500 }
        mockAxios.put.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            
            fs.readFile("./src/__mocks__/__mockData__/hourPayment.json", 'utf8', (err, data) => {
                const urlList = url.split("/")
                urlList.pop()
                urlList.pop()
                const hourPaymentId = urlList.pop()  
                if (err) reject(err)
              
                resolve({ data: JSON.parse(data).filter(hourPayment => 
                    hourPayment.id === +hourPaymentId ).shift() })
            })
          })
        )

        const data =  await hourPaymentService.update(hourPayment);
        
        expect(data).toEqual(hourPayment)
        expect(mockAxios.put).toHaveBeenCalledTimes(1);
        expect(mockAxios.put).toHaveBeenCalledWith(
            `${BASE_URL}project/${hourPayment.projectId}/hour_payment/${hourPayment.id}/update/`,
            {
                "id": 1,
                "projectId": 1,
                "rate": 500
            },
            {"headers": {}}
        );
    });

    it('test function Remove', async () => {

        const hourPayment = { id: 1, projectId: 1, rate: 500 }

        mockAxios.delete.mockImplementationOnce((url)=>
        new Promise((resolve, reject) => {
            
            fs.readFile("./src/__mocks__/__mockData__/hourPayment.json", 'utf8', (err, data) => {
                const urlList = url.split("/")
                urlList.pop()
                const hourPaymentId = urlList.pop()
                if (err) reject(err)
              
                resolve({ data: JSON.parse(data).filter(hourPayment => 
                    hourPayment.id === +hourPaymentId ).shift() })
            })
          })
        )

        const data =  await hourPaymentService.remove(hourPayment.id);
        expect(data).toEqual(hourPayment);
        expect(mockAxios.delete).toHaveBeenCalledTimes(1);
        
        expect(mockAxios.delete).toHaveBeenCalledWith(
            `${BASE_URL}project/hour_payment/${hourPayment.id}/delete`,
            {
                "headers": {}
            }
            
        )
    });
});