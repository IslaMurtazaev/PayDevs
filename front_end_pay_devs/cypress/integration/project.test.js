const baseUrl = "http://localhost:3000/";

describe("project", () => {
  let project = {
    id: 1,
    title: "Alpha bravo charlie",
    description: "Launch rocket to the Moon",
    type_of_payment: "T_P",
    start_date: "1999-08-02T10:00:00.000Z",
    end_date: "2018-09-03T10:25:13.779Z",
    status: false
  };

  let projects = [project];

  let tasks = [];

  beforeEach(() => {
    cy.login();
    cy.server();
    cy.route("GET", "http://127.0.0.1:8000/api/project/all", projects);
    cy.route("GET", `http://127.0.0.1:8000/api/project/${project.id}`, project);
    cy.route(
      "GET",
      `http://127.0.0.1:8000/api/project/${project.id}/task/all`,
      tasks
    );
  });

  it("creates new project", () => {
    cy.visit(baseUrl);

    cy.get(".newProjectLink")
      .click({ force: true })
      .url()
      .should("eq", `${baseUrl}project/create`);

    cy.get(".titleInput")
      .type(project.title)
      .should("have.value", project.title);
    cy.get(".descriptionInput")
      .type(project.description)
      .should("have.value", project.description);
    cy.get(".typeOfPaymentSelect")
      .select("Taskly")
      .should("have.value", project.type_of_payment);
    cy.get(".statusCheckbox")
      .uncheck({ force: true })
      .should("not.be.checked");

    cy.route("POST", "http://127.0.0.1:8000/api/project/create", project);

    cy.get(".form-group").submit();
    cy.url().should("eq", `${baseUrl}project/${project.id}`);

    cy.get(".projectTitle").should("contain", project.title);
    cy.get(".projectDescription").should("contain", project.description);
    cy.get(".projectStartDate").should(
      "contain",
      new Date(project.start_date).toDateString()
    );
    cy.get(".projectEndDate").should(
      "contain",
      new Date(project.end_date).toDateString()
    );
    cy.get(".projectTypeOfPayment").should("contain", "Taskly");
    cy.get(".projectStatus").should("contain", "not active");
  });

  it("updates project", () => {
    cy.visit(`${baseUrl}project/${project.id}`);

    cy.get(".updateProject").click();

    cy.url().should("eq", `${baseUrl}project/${project.id}/update`);

    cy.get(".titleInput").should("have.value", project.title);
    cy.get(".descriptionInput").should("have.value", project.description);
    cy.get(".typeOfPaymentSelect").should(
      "have.value",
      project.type_of_payment
    );
    cy.get(".statusCheckbox").should("not.be.checked");

    cy.get(".titleInput")
      .clear()
      .type("Alpha Bravo Whiskey")
      .should("have.value", "Alpha Bravo Whiskey");
    cy.get(".descriptionInput")
      .clear()
      .type("Colonize Mars")
      .should("have.value", "Colonize Mars");
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    let updatedProject = {
      id: 1,
      title: "Alpha Bravo Whiskey",
      description: "Colonize Mars",
      type_of_payment: "T_P",
      start_date: "1999-08-02T10:00:00.000Z",
      end_date: "2018-09-03T10:25:13.779Z",
      status: true
    };

    cy.route(
      "PUT",
      "http://127.0.0.1:8000/api/project/1/update/",
      updatedProject
    );

    cy.get(".form-group").submit();
    cy.url().should("eq", `${baseUrl}project/${project.id}`);

    cy.get(".projectTitle").should("contain", updatedProject.title);
    cy.get(".projectDescription").should("contain", updatedProject.description);
    cy.get(".projectStartDate").should(
      "contain",
      new Date(updatedProject.start_date).toDateString()
    );
    cy.get(".projectEndDate").should(
      "contain",
      new Date(updatedProject.end_date).toDateString()
    );
    cy.get(".projectTypeOfPayment").should("contain", "Taskly");
    cy.get(".projectStatus").should("contain", "active");

    project = updatedProject;
  });

  it("creates new task", () => {
    cy.visit(`${baseUrl}project/${project.id}`);

    const task = {
      id: 0,
      projectId: 0,
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
      `http://127.0.0.1:8000/api/project/${project.id}/task/create`,
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

  // it("updates task", () => {
  //   cy.get(".updateButton").click();
  // })

  it("creates second task", () => {
    cy.visit(`${baseUrl}project/${project.id}`);

    const task = {
      id: 1,
      projectId: 0,
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
      `http://127.0.0.1:8000/api/project/${project.id}/task/create`,
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
