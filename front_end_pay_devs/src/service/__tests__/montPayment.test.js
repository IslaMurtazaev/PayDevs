import mockAxios from "axios";
import monthPaymentService from "../monthPayment";

const fs = require("fs");

const BASE_URL = "/api/";

describe("Month Payment", async () => {
  it("test function getAll", async () => {
    const projectId = 1;
    const monthPayments = [
      { id: 1, projectId: 1, rate: 500 },
      { id: 2, projectId: 1, rate: 100 }
    ];
    mockAxios.get.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          const urlList = url.split("/");
          urlList.pop();
          urlList.pop();
          const projectId = urlList.pop();

          fs.readFile(
            "./src/__mocks__/__mockData__/monthPayment.json",
            "utf8",
            (err, data) => {
              if (err) reject(err);
              resolve({
                data: JSON.parse(data).filter(
                  monthPayment => monthPayment.projectId === +projectId
                )
              });
            }
          );
        })
    );

    const data = await monthPaymentService.getAll(projectId);
    expect(data).toEqual(monthPayments);
    expect(mockAxios.get).toHaveBeenCalledTimes(1);
    expect(mockAxios.get).toHaveBeenCalledWith(
      `${BASE_URL}project/${projectId}/month_payment/all`
    );
  });

  it("test function create", async () => {
    const monthPayment = { id: 1, projectId: 1, rate: 500 };
    mockAxios.post.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/monthPayment.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              urlList.pop();
              const projectId = urlList.pop();
              if (err) reject(err);
              resolve({
                data: JSON.parse(data)
                  .filter(monthPayment => monthPayment.projectId === +projectId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await monthPaymentService.create(
      monthPayment.projectId,
      monthPayment
    );

    expect(data).toEqual(monthPayment);
    expect(mockAxios.post).toHaveBeenCalledTimes(1);
    expect(mockAxios.post).toHaveBeenCalledWith(
      `${BASE_URL}project/${monthPayment.projectId}/month_payment/create`,
      {
        id: 1,
        projectId: 1,
        rate: 500
      }
    );
  });

  it("test function Remove", async () => {
    const monthPayment = { id: 1, projectId: 1, rate: 500 };

    mockAxios.delete.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/monthPayment.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              const monthPaymentId = urlList.pop();
              if (err) reject(err);

              resolve({
                data: JSON.parse(data)
                  .filter(monthPayment => monthPayment.id === +monthPaymentId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await monthPaymentService.remove(monthPayment.id);

    expect(data).toEqual(monthPayment);
    expect(mockAxios.delete).toHaveBeenCalledTimes(1);

    expect(mockAxios.delete).toHaveBeenCalledWith(
      `${BASE_URL}project/month_payment/${monthPayment.id}/delete`
    );
  });
});
