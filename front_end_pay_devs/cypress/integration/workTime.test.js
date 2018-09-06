const baseUrl = "http://localhost:3000/";
describe("Work Time", () => {
  let project = {
    id: 1,
    title: "Alpha bravo charlie",
    description: "Launch rocket to the Moon",
    type_of_payment: "H_P",
    start_date: "1999-08-02T10:00:00.000Z",
    end_date: "2018-09-03T10:25:13.779Z",
    status: false
  };

  beforeEach(() => {
    cy.login();
    cy.server();
  });

  it("Create Work Time", () => {
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
      .select("Hourly")
      .should("have.value", project.type_of_payment);
    cy.get(".statusCheckbox")
      .check({ force: true })
      .should("be.checked");

    cy.get(".form-group").submit();

    cy.get(".projectTitle").should("contain", project.title);
    cy.get(".projectDescription").should("contain", project.description);
    cy.get(".rateHourPaymnet").clear();
    cy.get(".rateHourPaymnet")
      .type(rate)
      .should("have.value", rate);
    cy.get(".newRateHourPayment").click({ force: true });
    cy.get(".workTimes").click({ force: true });
    cy.get(".workTimePaid")
      .check({ force: true })
      .should("be.checked");
    cy.get(".worked-time-form").submit();
    cy.get(".paid").should("contain", "paid");
    // cy.get(".newRateHourPayment").click({ force: true });
    // cy.get(".removeRate").click({ force: true });
    // cy.get(".removeProject").click({ force: true });
  });

  it("Update workTime ", () => {
    cy.visit(baseUrl);
    cy.get(".projectLink").click({ force: true });
    cy.get(".workTimes").click({ force: true });
    cy.get(".updateWorkTime").click();
    cy.get(".workTimePaid")
      .uncheck({ force: true })
      .should("not.be.checked");
    cy.get(".worked-time-form").submit();
    cy.get(".paid").should("contain", "not paid");
  });

  it("remove work time", () => {
    cy.visit(baseUrl);
    cy.get(".projectLink").click({ force: true });
    cy.get(".workTimes").click({ force: true });
    cy.get(".paid").should("contain", "not paid");
    cy.get(".removeWorkTime").click({ force: true });
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
