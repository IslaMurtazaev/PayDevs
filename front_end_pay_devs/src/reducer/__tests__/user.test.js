import user from "../user";
import { userConstants } from "../../constants/user";

describe("user reducer", () => {
  it("has a default state", () => {
    const defaultState = {};
    const action = { type: "NOT_MATCHING_ACTION" };

    expect(user(undefined, action)).toEqual(defaultState);
  });

  it("triggers LOGIN_USER", () => {
    const loggedUser = { username: "IslaMurtazaev", password: "CapeTown" };
    const action = { type: userConstants.LOGIN_USER, user: loggedUser };

    expect(user({}, action)).toEqual({user: loggedUser});
  });

  it("triggers LOGIN_ERROR", () => {
    const error = { error_message: "Access denied!" };
    const action = { type: userConstants.LOGIN_ERROR, error };

    expect(user({}, action)).toEqual({error: error});
  });
});
