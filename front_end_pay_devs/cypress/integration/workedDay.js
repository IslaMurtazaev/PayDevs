const baseUrl = "http://localhost:3000/";
describe("Work Day", () => {
  let project = {
    id: 1,
    title: "Alpha bravo charlie",
    description: "Launch rocket to the Moon",
    type_of_payment: "M_P",
    start_date: "1999-08-02T10:00:00.000Z",
    end_date: "2018-09-03T10:25:13.779Z",
    status: false
  };

  beforeEach(() => {
    cy.login();
    cy.server();
  });
  it("creates work day", () => {
    const rate = "5000";
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
      .select("Monthly")
      .should("have.value", project.type_of_payment);
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.get(".form-group").submit();
    cy.get(".projectTitle").should("contain", project.title);
    cy.get(".projectDescription").should("contain", project.description);
    cy.get(".rateMonthPaymnet").clear();
    cy.get(".rateMonthPaymnet")
      .type(rate)
      .should("have.value", rate);
    cy.get(".newRateMonthPayment").click({ force: true });
    cy.get(".workDays").click({ force: true });
    cy.get(".workDayPaid")
      .check({ force: true })
      .should("be.checked");
    cy.get(".dayWokedDay")
      .type("2018-01-01")
      .should("have.value", "2018-01-01");
    cy.get(".worked-day-form").submit();
    cy.get(".paid").should("contain", "paid");
  });

  it("updates work day", () => {
    cy.visit(baseUrl);
    cy.get(".projectLink").click({ force: true });
    cy.get(".workDays").click({ force: true });
    cy.get(".updateWorkedDay").click();
    cy.get(".workDayPaid")
      .uncheck({ force: true })
      .should("not.be.checked");
    cy.get(".worked-day-form").submit();
    cy.get(".paid").should("contain", "not paid");
  });

  it("removes work day", () => {
    cy.visit(baseUrl);
    cy.get(".projectLink").click({ force: true });
    cy.get(".workDays").click({ force: true });
    cy.get(".paid").should("contain", "not paid");
    cy.get(".removeWorkDay").click({ force: true });
    cy.get(".paid").should("not.contain", "not paid");
    cy.visit(baseUrl);
    cy.get(".projectLink").click({ force: true });
    cy.get(".removeRate").click({ force: true });
    cy.get(".removeProject").click({ force: true });
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
