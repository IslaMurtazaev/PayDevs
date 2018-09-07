const baseUrl = "http://localhost:3000/";

describe("Project", () => {
  let projectTaskly = {
    id: 1,
    title: "Alpha bravo charlie",
    description: "Launch rocket to the Moon",
    type_of_payment: "T_P",
    start_date: "1999-08-02T10:00:00.000Z",
    end_date: "2018-09-03T10:25:13.779Z",
    status: false
  };
  let projectMonthly = {
    id: 2,
    title: "Internship in IT-Attractor",
    description: "The best place to have practice",
    type_of_payment: "M_P",
    start_date: "2018-06-18T08:00:00.000Z",
    end_date: "2018-09-07T10:25:13.779Z",
    status: true
  };
  let projectHourly = {
    id: 3,
    title: "TopTal",
    description: "Top talanted guys",
    type_of_payment: "H_P",
    start_date: "2018-06-18T08:00:00.000Z",
    end_date: "2018-09-07T10:25:13.779Z",
    status: true
  };
  let projects = [];

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
      `http://127.0.0.1:8000/api/project/${projectMonthly.id}`,
      projectMonthly
    );
    cy.route(
      "GET",
      `http://127.0.0.1:8000/api/project/${projectHourly.id}`,
      projectHourly
    );
    cy.route(
      "GET",
      `http://127.0.0.1:8000/api/project/${projectTaskly.id}/task/all`,
      []
    );
  });

  it("creates new taskly project", () => {
    cy.visit(baseUrl);

    cy.get(".newProjectLink")
      .click({ force: true })
      .url()
      .should("eq", `${baseUrl}project/create`);

    cy.get(".titleInput")
      .type(projectTaskly.title)
      .should("have.value", projectTaskly.title);
    cy.get(".descriptionInput")
      .type(projectTaskly.description)
      .should("have.value", projectTaskly.description);
    cy.get(".typeOfPaymentSelect")
      .select("Taskly")
      .should("have.value", projectTaskly.type_of_payment);
    cy.get(".statusCheckbox")
      .uncheck({ force: true })
      .should("not.be.checked");

    cy.route("POST", "http://127.0.0.1:8000/api/project/create", projectTaskly);

    cy.get(".form-group").submit();
    projects.push(projectTaskly);
    cy.url().should("eq", `${baseUrl}project/${projectTaskly.id}`);

    cy.get(".projectTitle").should("contain", projectTaskly.title);
    cy.get(".projectDescription").should("contain", projectTaskly.description);
    cy.get(".projectStartDate").should(
      "contain",
      new Date(projectTaskly.start_date).toDateString()
    );
    cy.get(".projectEndDate").should(
      "contain",
      new Date(projectTaskly.end_date).toDateString()
    );
    cy.get(".projectTypeOfPayment").should("contain", "Taskly");
    cy.get(".projectStatus").should("contain", "not active");

    cy.visit(baseUrl);
    cy.get(".projectList ul li")
      .its("length")
      .should("eq", 1);
    cy.get(".projectList").should("contain", projectTaskly.title);
  });

  it("creates new monthly project", () => {
    cy.visit(baseUrl);

    cy.get(".newProjectLink")
      .click({ force: true })
      .url()
      .should("eq", `${baseUrl}project/create`);

    cy.get(".titleInput")
      .type(projectMonthly.title)
      .should("have.value", projectMonthly.title);
    cy.get(".descriptionInput")
      .type(projectMonthly.description)
      .should("have.value", projectMonthly.description);
    cy.get(".typeOfPaymentSelect")
      .select("Monthly")
      .should("have.value", projectMonthly.type_of_payment);
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "POST",
      "http://127.0.0.1:8000/api/project/create",
      projectMonthly
    );

    cy.get(".form-group").submit();
    projects.push(projectMonthly);
    cy.url().should("eq", `${baseUrl}project/${projectMonthly.id}`);

    cy.get(".projectTitle").should("contain", projectMonthly.title);
    cy.get(".projectDescription").should("contain", projectMonthly.description);
    cy.get(".projectStartDate").should(
      "contain",
      new Date(projectMonthly.start_date).toDateString()
    );
    cy.get(".projectEndDate").should(
      "contain",
      new Date(projectMonthly.end_date).toDateString()
    );
    cy.get(".projectTypeOfPayment").should("contain", "Monthly");
    cy.get(".projectStatus").should("not.contain", "not");

    cy.visit(baseUrl);
    cy.get(".projectList ul li")
      .its("length")
      .should("eq", 2);
    cy.get(".projectList").should("contain", projectMonthly.title);
  });

  it("creates new hourly project", () => {
    cy.visit(baseUrl);

    cy.get(".newProjectLink")
      .click({ force: true })
      .url()
      .should("eq", `${baseUrl}project/create`);

    cy.get(".titleInput")
      .type(projectHourly.title)
      .should("have.value", projectHourly.title);
    cy.get(".descriptionInput")
      .type(projectHourly.description)
      .should("have.value", projectHourly.description);
    cy.get(".typeOfPaymentSelect")
      .select("Hourly")
      .should("have.value", projectHourly.type_of_payment);
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route("POST", "http://127.0.0.1:8000/api/project/create", projectHourly);

    cy.get(".form-group").submit();
    projects.push(projectHourly);
    cy.url().should("eq", `${baseUrl}project/${projectHourly.id}`);

    cy.get(".projectTitle").should("contain", projectHourly.title);
    cy.get(".projectDescription").should("contain", projectHourly.description);
    cy.get(".projectStartDate").should(
      "contain",
      new Date(projectHourly.start_date).toDateString()
    );
    cy.get(".projectEndDate").should(
      "contain",
      new Date(projectHourly.end_date).toDateString()
    );
    cy.get(".projectTypeOfPayment").should("contain", "Hourly");
    cy.get(".projectStatus").should("not.contain", "not");

    cy.visit(baseUrl);
    cy.get(".projectList ul li")
      .its("length")
      .should("eq", 3);
    cy.get(".projectList").should("contain", projectHourly.title);
  });

  it("updates project", () => {
    cy.visit(`${baseUrl}project/${projectTaskly.id}`);

    cy.get(".updateProject").click();

    cy.url().should("eq", `${baseUrl}project/${projectTaskly.id}/update`);

    cy.get(".titleInput").should("have.value", projectTaskly.title);
    cy.get(".descriptionInput").should("have.value", projectTaskly.description);
    cy.get(".typeOfPaymentSelect").should(
      "have.value",
      projectTaskly.type_of_payment
    );
    cy.get(".statusCheckbox").should("not.be.checked");

    let updatedProject = {
      id: 1,
      title: "Alpha Bravo Whiskey",
      description: "Colonize Mars",
      type_of_payment: "T_P",
      start_date: "1999-08-02T10:00:00.000Z",
      end_date: "2018-09-03T10:25:13.779Z",
      status: true
    };

    cy.get(".titleInput")
      .clear()
      .type(updatedProject.title)
      .should("have.value", updatedProject.title);
    cy.get(".descriptionInput")
      .clear()
      .type(updatedProject.description)
      .should("have.value", updatedProject.description);
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.route(
      "PUT",
      "http://127.0.0.1:8000/api/project/1/update/",
      updatedProject
    );

    cy.get(".form-group").submit();
    cy.url().should("eq", `${baseUrl}project/${projectTaskly.id}`);

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
    cy.get(".projectStatus").should("not.contain", "not");

    projectTaskly = updatedProject;
    projects[0] = projectTaskly;
  });

  it("deletes project", () => {
    let projectToDelete = {
      title: "Delete me",
      description: "Sun is going down",
      type_of_payment: "T_P",
      start_date: "1999-08-02T10:00:00.000Z",
      end_date: "2018-09-03T10:25:13.779Z",
      status: false
    };

    cy.server({ enable: false });

    cy.visit(`${baseUrl}project/create`);
    cy.get(".titleInput").type(projectToDelete.title);
    cy.get(".descriptionInput").type(projectToDelete.description);

    cy.get(".form-group").submit();

    cy.visit(baseUrl);
    cy.get(".projectList ul li")
      .its("length")
      .should("eq", 1);
    cy.get(".projectList").should("contain", projectToDelete.title);

    cy.get(".projectLink").click();
    cy.get(".removeProject").click();

    cy.url().should("eq", baseUrl);
    cy.get(".projectList").should("not.contain", projectToDelete.title);
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
