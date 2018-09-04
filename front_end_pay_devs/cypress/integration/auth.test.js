const username = "MonkeyTester";
const email = "ilove@banana.com";
const password = "qwerty123";
const baseUrl = "http://localhost:3000/";

describe("Sign up", () => {
  it("signs up new user", () => {
    cy.visit(`${baseUrl}sign_up`);

    cy.get(".usernameInput")
      .type(username)
      .should("have.value", username);
    cy.get(".emailInput")
      .type(email)
      .should("have.value", email);
    cy.get(".passwordInput")
      .type(password)
      .should("have.value", password)
      .type("{enter}");
  });
});

describe("Login", () => {
  it("logins existing user", () => {
    cy.visit(baseUrl);
    cy.url().should("eq", `${baseUrl}login`);

    cy.get(".usernameInput")
      .type(username)
      .should("have.value", username);
    cy.get(".passwordInput")
      .type(password)
      .should("have.value", password)
      .type("{enter}")
      .should(() => {
        let { id, token,  ...user } = JSON.parse(localStorage.getItem("user"));
        expect(user).to.eql({
          email: email,
          is_active: true,
          username: username,
          is_staff: false,
        });
      });
    cy.url().should("eq", `${baseUrl}`);
  });

  it("logs out the user", () => {
    cy.get(".logout").click();
    cy.url().should("eq", `${baseUrl}login`);
  });

  it("tries to login without fullfiling the form", () => {
    cy.get(".usernameInput").clear();
    cy.get(".loginForm").submit();
    cy.get(".help-block").should("contain", "Username is required");

    cy.get(".usernameInput").type(username);
    cy.get(".passwordInput").clear();
    cy.get(".loginForm").submit();
    cy.get(".help-block").should("contain", "Password is required");

    cy.get(".passwordInput").type(password);
    cy.get(".loginForm")
      .submit()
      .should(() => {
        let { id, token, ...user } = JSON.parse(localStorage.getItem("user"));
        expect(user).to.eql({
          email: email,
          is_active: true,
          username: username,
          is_staff: false,
        });
      });
    cy.url().should("eq", `${baseUrl}`);
  });
});
