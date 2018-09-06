const baseUrl = "http://localhost:3000/";

describe("task", () => {
  beforeEach(() => {
    cy.login();
    cy.server();
    cy.route("GET", "http://127.0.0.1:8000/api/project/all", projects);
    cy.route(
      "GET",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}`,
      projectTaskly
    );
    cy.route(
      "GET",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/all`,
      tasks
    );
  });
  let projectTaskly = {
    id: 1,
    title: "Alpha bravo charlie",
    description: "Launch rocket to the Moon",
    type_of_payment: "T_P",
    start_date: "1999-08-02T10:00:00.000Z",
    end_date: "2018-09-03T10:25:13.779Z",
    status: false
  };
  let projects = [projectTaskly];
  let tasks = [];

  it("creates new task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);

    const task = {
      id: 1,
      projectId: 1,
      title: "finish these damn tests",
      description: "why it has to be so long?",
      price: 100000,
      paid: true,
      completed: true
    };

    cy.get(".titleInput")
      .type(task.title)
      .should("have.value", task.title);
    cy.get(".descriptionInput")
      .type(task.description)
      .should("have.value", task.description);
    cy.get(".priceInput")
      .type(task.price)
      .should("have.value", task.price.toString());
    cy.get(".paidCheckbox")
      .check({ force: true })
      .should("be.checked");
    cy.get(".completedCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "POST",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/create`,
      task
    );

    cy.get(".task-form")
      .submit()
      .then(() => {
        tasks.push(task);
      });

    cy.get(".taskTitle").should("contain", task.title);
    cy.get(".taskDescription").should("contain", task.description);
    cy.get(".taskPrice").should("contain", task.price);
    cy.get(".taskPaid").should("contain", "paid");
    cy.get(".taskCompleted").should("contain", "Completed");
  });

  it("creates second task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);

    const task = {
      id: 2,
      projectId: 1,
      title: "read clean code",
      description: "the only pleasure after long day",
      price: 1000000,
      paid: false,
      completed: false
    };

    cy.get(".titleInput")
      .type(task.title)
      .should("have.value", task.title);
    cy.get(".descriptionInput")
      .type(task.description)
      .should("have.value", task.description);
    cy.get(".priceInput")
      .type(task.price)
      .should("have.value", task.price.toString());
    cy.get(".paidCheckbox")
      .check({ force: true })
      .should("be.checked");
    cy.get(".completedCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "POST",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/create`,
      task
    );

    cy.get(".task-form")
      .submit()
      .then(() => {
        tasks.push(task);
      });

    cy.get(".taskTitle").should("contain", task.title);
    cy.get(".taskDescription").should("contain", task.description);
    cy.get(".taskPrice").should("contain", task.price);
    cy.get(".taskPaid").should("contain", "not paid");
    cy.get(".taskCompleted").should("contain", "Uncompleted");
  });
});

Cypress.Commands.add("login", () => {
  cy.request({
    method: "POST",
    url: "http://127.0.0.1:8000/api/users/login",
    body: JSON.stringify({
      username: "MonkeyTester",
      password: "qwerty123"
    })
  }).then(resp => {
    window.localStorage.setItem("user", JSON.stringify(resp.body));
  });
});

Cypress.Commands.add("createProject", (project, userToken) => {
  cy.request({
    method: "POST",
    url: "http://127.0.0.1:8000/api/project/create",
    headers: { Authorization: userToken },
    body: JSON.stringify(project)
  });
});
