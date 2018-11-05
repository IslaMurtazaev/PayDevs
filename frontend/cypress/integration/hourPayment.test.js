const baseUrl = "http://localhost:3000/";

describe("Hour Payment", () => {
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

  it("create and remoute hour payment", () => {
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

    cy.get(".rate").then($rate => {
      expect($rate.text()).to.eq("5000/per hour");
    });
    cy.get(".hourlyRates").should(
      "contain",
      "Select one of your current rates:"
    );
    cy.get(".hourlyRates").should("contain", "5000/per hour");

    cy.get(".removeRate").click({ force: true });
    cy.get(".hourlyRates").should(
      "not.contain",
      "Select one of your current rates:"
    );
    cy.get(".hourlyRates").should("not.contain", "5000/per hour");
    cy.get(".removeProject").click({ force: true });
  });
});

Cypress.Commands.add("login", () => {
  cy.request({
    method: "POST",
    url: "http://localhost:8000/api/users/login",
    body: JSON.stringify({
      username: "MonkeyTester",
      password: "qwerty123"
    })
  }).then(resp => {
    window.localStorage.setItem("user", JSON.stringify(resp.body));
  });
});
