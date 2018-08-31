import configureMockStore from "redux-mock-store";
import thunk from "redux-thunk";
import { UserService } from "service/user";
import { userActions } from "../user";
import { userActionTypes } from "../../constants/user";
jest.mock("../../service/user", () => require("service/user"));
jest.mock("../../service/helpers", () => require("helpers"));
jest.mock("../../index", () => require("history"));

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe("actions Worked Day", () => {
  it("should authentication an action to add a todo", async () => {
    const user = {
      id: 1,
      username: "test",
      email: "test@mail.ru",
      password: "qwert112345"
    };
    const expectedAction = {
      type: userActionTypes.LOGIN_USER,
      user
    };
    UserService.login.mockImplementationOnce((username, password) => {
      return Promise.resolve(user);
    });

    const store = mockStore({});

    return store
      .dispatch(userActions.authentication(user.username, user.password))
      .then(() => {
        const action = store.getActions();
        expect(action.length).toBe(1);
        expect(action).toContainEqual(expectedAction);
        expect(UserService.login).toHaveBeenCalledTimes(1);
      });
  });
  it("should sing_up an action to add a todo", async () => {
    const user = {
      id: 1,
      username: "test",
      email: "test@mail.ru",
      password: "qwert112345"
    };
    const expectedAction = {
      type: userActionTypes.LOGIN_USER,
      user
    };
    UserService.create_user.mockImplementationOnce(
      (username, email, password) => {
        return Promise.resolve(user);
      }
    );

    const store = mockStore({});

    return store
      .dispatch(userActions.sign_up(user.username, user.email, user.password))
      .then(() => {
        const action = store.getActions();
        expect(action.length).toBe(1);
        expect(action).toContainEqual(expectedAction);
        expect(UserService.create_user).toHaveBeenCalledTimes(1);
      });
  });

  it("should logout an action to add a todo", async () => {
    const expectedAction = {
      type: userActionTypes.LOGOUT
    };

    const store = mockStore({});

    store.dispatch(userActions.logout());
    const action = store.getActions();
    expect(action.length).toBe(1);
    expect(action.pop()).toEqual(expectedAction);
  });
});
