const baseUrl = "http://localhost:3000/";

describe("Task", () => {
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

  let task1 = {
    id: 1,
    project_id: 1,
    title: "finish these damn tests",
    description: "why it has to be so long?",
    price: 100000,
    paid: false,
    completed: false
  };
  let task2 = {
    id: 2,
    project_id: 1,
    title: "read clean code",
    description: "the only pleasure after long day",
    price: 1000000,
    paid: true,
    completed: true
  };
  let tasks = [];

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

  it("creates new task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);

    cy.get(".titleInput")
      .type(task1.title)
      .should("have.value", task1.title);
    cy.get(".descriptionInput")
      .type(task1.description)
      .should("have.value", task1.description);
    cy.get(".priceInput")
      .type(task1.price)
      .should("have.value", task1.price.toString());
    cy.get(".paidCheckbox")
      .uncheck({ force: true })
      .should("not.be.checked");
    cy.get(".completedCheckbox")
      .uncheck({ force: true })
      .should("not.be.checked");

    cy.route(
      "POST",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/create`,
      task1
    );

    cy.get(".task-form")
      .submit()
      .then(() => {
        tasks.push(task1);
      });

    cy.get(".taskTitle").should("contain", task1.title);
    cy.get(".taskDescription").should("contain", task1.description);
    cy.get(".taskPrice").should("contain", task1.price);
    cy.get(".taskPaid").should("contain", "not paid");
    cy.get(".taskCompleted").should("contain", "Uncompleted");
  });

  it("creates second task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);

    cy.get(".titleInput")
      .type(task2.title)
      .should("have.value", task2.title);
    cy.get(".descriptionInput")
      .type(task2.description)
      .should("have.value", task2.description);
    cy.get(".priceInput")
      .type(task2.price)
      .should("have.value", task2.price.toString());
    cy.get(".paidCheckbox")
      .check({ force: true })
      .should("be.checked");
    cy.get(".completedCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "POST",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/create`,
      task2
    );

    cy.get(".task-form")
      .submit()
      .then(() => {
        tasks.push(task2);
      });

    cy.get(".taskTitle").should("contain", task2.title);
    cy.get(".taskDescription").should("contain", task2.description);
    cy.get(".taskPrice").should("contain", task2.price);
    cy.get(".taskPaid").should("contain", "not paid");
    cy.get(".taskCompleted").should("contain", "Uncompleted");
  });

  it("updates task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);
    cy.get(".updateButton")
      .first()
      .click();
    cy.url().should(
      "eq",
      `${baseUrl}project/${projectTaskly.id}/Taskly/${task1.id}/update`
    );

    const updatedTask = {
      id: 1,
      project_id: 1,
      title: "Finish them",
      description: "At least cypress makes it easier",
      price: 1000000,
      paid: true,
      completed: true
    };

    cy.get(".titleInput")
      .clear()
      .type(updatedTask.title)
      .should("have.value", updatedTask.title);
    cy.get(".descriptionInput")
      .clear()
      .type(updatedTask.description)
      .should("have.value", updatedTask.description);
    cy.get(".priceInput")
      .clear()
      .type(updatedTask.price)
      .should("have.value", updatedTask.price.toString());
    cy.get(".paidCheckbox")
      .check({ force: true })
      .should("be.checked");
    cy.get(".completedCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "PUT",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/${
        task1.id
      }/update/`,
      updatedTask
    );

    cy.get(".task-form").submit();
    task1 = updatedTask;
    tasks[0] = task1;

    cy.url().should("eq", `${baseUrl}project/${projectTaskly.id}`);

    cy.get(".taskTitle").should("contain", updatedTask.title);
    cy.get(".taskDescription").should("contain", updatedTask.description);
    cy.get(".taskPrice").should("contain", updatedTask.price);
    cy.get(".taskPaid").should("contain", "paid");
    cy.get(".taskCompleted").should("contain", "Completed");
  });

  it("deletes task", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);
    cy.get(".task").its("length").should("eq", 2)
    cy.get(".tasks").should("contain", task2.title);

    cy.route(
      "DELETE",
      `http://127.0.0.1:8000/api/project/task/${task2.id}/delete`,
      task2
    );
    cy.get(".removeButton").last().click();

    cy.get(".tasks").should("not.contain", task2.title);
    cy.get(".task").its("length").should("eq", 1)
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
