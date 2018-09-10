import mockAxios from "axios";
import { projectService } from "../project";
const fs = require("fs");

const BASE_URL = "/api/";

describe("Project", async () => {
  it("test function getAll", async () => {
    const userId = 1;

    const projects = [
      {
        id: 1,
        user_id: 1,
        title: "Project web  Task Payment",
        description: "logic web sites",
        start_date: "2017-12-20T04:00:00.000000Z",
        end_date: "2018-08-27T11:48:07.601329Z",
        status: true,
        type_of_payment: "T_P"
      },
      {
        id: 2,
        user_id: 1,
        title: "Project web  Month Payment",
        description: "logic web sites",
        start_date: "2017-12-20T04:00:00.000000Z",
        end_date: "2018-08-27T11:48:07.601329Z",
        status: true,
        type_of_payment: "M_P"
      }
    ];
    mockAxios.get.mockImplementationOnce(
      () =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/project.json",
            "utf8",
            (err, data) => {
              if (err) reject(err);
              resolve({
                data: JSON.parse(data).filter(
                  project => project.user_id === userId
                )
              });
            }
          );
        })
    );

    const data = await projectService.getAll();

    expect(data).toEqual(projects);
    expect(mockAxios.get).toHaveBeenCalledTimes(1);
    expect(mockAxios.get).toHaveBeenCalledWith(`${BASE_URL}project/all`);
  });

  it("test function create", async () => {
    const userId = 1;
    const project = {
      id: 1,
      user_id: 1,
      title: "Project web  Task Payment",
      description: "logic web sites",
      start_date: "2017-12-20T04:00:00.000000Z",
      end_date: "2018-08-27T11:48:07.601329Z",
      status: true,
      type_of_payment: "T_P"
    };
    mockAxios.post.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/project.json",
            "utf8",
            (err, data) => {
              if (err) reject(err);

              resolve({
                data: JSON.parse(data)
                  .filter(project => project.user_id === userId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await projectService.create(project);
    expect(data).toEqual(project);
    expect(mockAxios.post).toHaveBeenCalledTimes(1);
    expect(mockAxios.post).toHaveBeenCalledWith(`${BASE_URL}project/create`, {
      id: 1,
      user_id: 1,
      title: "Project web  Task Payment",
      description: "logic web sites",
      start_date: "2017-12-20T04:00:00.000000Z",
      end_date: "2018-08-27T11:48:07.601329Z",
      status: true,
      type_of_payment: "T_P"
    });
  });

  it("test function Update", async () => {
    const project = {
      id: 1,
      user_id: 1,
      title: "Project web  Task Payment",
      description: "logic web sites",
      start_date: "2017-12-20T04:00:00.000000Z",
      end_date: "2018-08-27T11:48:07.601329Z",
      status: true,
      type_of_payment: "T_P"
    };
    mockAxios.put.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/project.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              const projectId = urlList.pop();
              if (err) reject(err);
              resolve({
                data: JSON.parse(data)
                  .filter(project => project.id === +projectId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await projectService.update(project);
    expect(data).toEqual(project);
    expect(mockAxios.put).toHaveBeenCalledTimes(1);
    expect(mockAxios.put).toHaveBeenCalledWith(
      `${BASE_URL}project/${project.id}/update`,
      {
        id: 1,
        user_id: 1,
        title: "Project web  Task Payment",
        description: "logic web sites",
        start_date: "2017-12-20T04:00:00.000000Z",
        end_date: "2018-08-27T11:48:07.601329Z",
        status: true,
        type_of_payment: "T_P"
      }
    );
  });

  it("test function Remove", async () => {
    const project = {
      id: 1,
      user_id: 1,
      title: "Project web  Task Payment",
      description: "logic web sites",
      start_date: "2017-12-20T04:00:00.000000Z",
      end_date: "2018-08-27T11:48:07.601329Z",
      status: true,
      type_of_payment: "T_P"
    };
    mockAxios.delete.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/project.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              urlList.pop();
              const projectId = urlList.pop();
              if (err) reject(err);
              resolve({
                data: JSON.parse(data)
                  .filter(project => project.id === +projectId)
                  .shift()
              });
            }
          );
        })
    );

    const data = await projectService.remove(project.id);

    expect(data).toEqual(project);
    expect(mockAxios.delete).toHaveBeenCalledTimes(1);

    expect(mockAxios.delete).toHaveBeenCalledWith(
      `${BASE_URL}project/${project.id}/delete`
    );
  });
  it("test function Get", async () => {
    const project = {
      id: 1,
      user_id: 1,
      title: "Project web  Task Payment",
      description: "logic web sites",
      start_date: "2017-12-20T04:00:00.000000Z",
      end_date: "2018-08-27T11:48:07.601329Z",
      status: true,
      type_of_payment: "T_P"
    };
    mockAxios.get.mockImplementationOnce(
      url =>
        new Promise((resolve, reject) => {
          fs.readFile(
            "./src/__mocks__/__mockData__/project.json",
            "utf8",
            (err, data) => {
              const urlList = url.split("/");
              const projectId = urlList.pop();
              if (err) reject(err);
              resolve({
                data: JSON.parse(data)
                  .filter(project => project.id === +projectId)
                  .pop()
              });
            }
          );
        })
    );

    const data = await projectService.get(project.id);
    expect(data).toEqual(project);
    expect(mockAxios.get).toHaveBeenCalledTimes(2);

    expect(mockAxios.get).toHaveBeenCalledWith(
      `${BASE_URL}project/${project.id}`
    );
  });
});
