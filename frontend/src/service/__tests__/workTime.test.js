import mockAxios from "axios";
import { workTimeService } from "../workTime";
jest.mock("../helpers", () => require("axios"));
const fs = require("fs");
const BASE_URL = "/api/";

describe("Worked Time", async () => {
  const hourPaymentId = 1;
  const workTimes = [
    {
      id: 1,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1
    },
    {
      id: 2,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1
    }
  ];
  it("test function getAll", async () => {
    mockAxios.get.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          const urlList = url.split("/");
          urlList.pop();
          urlList.pop();
          const hourPaymnetId = urlList.pop();

          fs.readFile(
            "./src/__mocks__/__mockData__/workTime.json",
            "utf8",
            (err, data) => {
              if (err) reject(err);
              resolve({
                data: JSON.parse(data).filter(
                  workTime => workTime.hourPaymentId === +hourPaymnetId
                )
              });
            }
          );
        })
    );

    const data = await workTimeService.getAll(hourPaymentId);
    expect(data).toEqual(workTimes);
    expect(mockAxios.get).toHaveBeenCalledTimes(1);
    expect(mockAxios.get).toHaveBeenCalledWith(
      `${BASE_URL}project/hour_payment/${hourPaymentId}/work_time/all`
    );
  });
  it("test function create", async () => {
    const workTime = {
      id: 1,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1,
      projectId: 1
    };
    mockAxios.post.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/workTime.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              urlList.pop();
              const hourPaymentId = urlList.pop();

              if (err) reject(err);

              resolve({
                data: JSON.parse(data)
                  .filter(workTime => workTime.hourPaymentId === +hourPaymentId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await workTimeService.create(workTime);

    expect(data).toEqual({
      id: 1,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1
    });
    expect(mockAxios.post).toHaveBeenCalledTimes(1);

    expect(mockAxios.post).toHaveBeenCalledWith(
      `${BASE_URL}project/${workTime.projectId}/hour_payment/${
        workTime.hourPaymentId
      }/work_time/create`,
      {
        id: 1,
        start_work: "2018-08-27T12:03:41.543000Z",
        end_work: "2018-08-27T12:03:41.543000Z",
        paid: false,
        hourPaymentId: 1,
        projectId: 1
      }
    );
  });

  it("test function Update", async () => {
    const projectId = 1;

    const workTime = {
      id: 1,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1
    };

    mockAxios.put.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/workTime.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              const workTimeId = urlList.pop();
              if (err) reject(err);

              resolve({
                data: JSON.parse(data)
                  .filter(workTime => workTime.id === +workTimeId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await workTimeService.update(
      projectId,
      workTime.hourPaymentId,
      workTime.id,
      workTime
    );
    expect(data).toEqual(workTime);
    expect(mockAxios.put).toHaveBeenCalledTimes(1);

    expect(mockAxios.put).toHaveBeenCalledWith(
      `${BASE_URL}project/${projectId}/hour_payment/${
        workTime.hourPaymentId
      }/work_time/${workTime.id}/update`,
      {
        id: 1,
        start_work: "2018-08-27T12:03:41.543000Z",
        end_work: "2018-08-27T12:03:41.543000Z",
        paid: false,
        hourPaymentId: 1
      }
    );
  });
  it("test function Remove", async () => {
    const workTime = {
      id: 1,
      start_work: "2018-08-27T12:03:41.543000Z",
      end_work: "2018-08-27T12:03:41.543000Z",
      paid: false,
      hourPaymentId: 1
    };

    mockAxios.delete.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/workTime.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              const workTimeId = urlList.pop();

              if (err) reject(err);

              resolve({
                data: JSON.parse(data)
                  .filter(workTime => workTime.id === +workTimeId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await workTimeService.remove(workTime.id);

    expect(data).toEqual(workTime);
    expect(mockAxios.delete).toHaveBeenCalledTimes(1);

    expect(mockAxios.delete).toHaveBeenCalledWith(
      `${BASE_URL}project/work_time/${workTime.id}/delete`
    );
  });
});
