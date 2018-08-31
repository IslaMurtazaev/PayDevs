import monthPaymentActions from "../monthPayment";
import { monthPaymentActionTypes } from "../../constants/monthPayment";
import monthPaymentService from "service/monthPayment";
import configureMockStore from "redux-mock-store";
import thunk from "redux-thunk";
jest.mock("../../service/monthPayment", () => require("service/monthPayment"));
jest.mock("../../service/helpers", () => require("helpers"));

const middlewares = [thunk];
const mockStore = configureMockStore(middlewares);

describe("actions month paymnet", () => {
  it("should getAll an action to add a todo", async () => {
    const projectId = 1;
    const expectedAction = {
      type: monthPaymentActionTypes.ADD_ALL,
      monthPayments: ["monthPayment"]
    };
    monthPaymentService.getAll.mockImplementationOnce(projectId => {
      return Promise.resolve(["monthPayment"]);
    });

    const store = mockStore({});

    return store.dispatch(monthPaymentActions.getAll(projectId)).then(() => {
      const action = store.getActions();
      expect(action.length).toBe(1);
      expect(action).toContainEqual(expectedAction);
      expect(monthPaymentService.getAll).toHaveBeenCalledTimes(1);
    });
  });
  it("should getAll an action to add a todo", async () => {
    const monthPayment = { id: 1, projectId: 1, rate: 500 };
    const expectedAction = {
      type: monthPaymentActionTypes.CREATE,
      monthPayment
    };
    monthPaymentService.create.mockImplementationOnce(
      (projectId, monthPayment) => {
        return Promise.resolve(monthPayment);
      }
    );

    const store = mockStore({});

    return store
      .dispatch(
        monthPaymentActions.create(monthPayment.projectId, monthPayment)
      )
      .then(() => {
        const action = store.getActions();
        expect(action.length).toBe(1);
        expect(action).toContainEqual(expectedAction);
        expect(monthPaymentService.create).toHaveBeenCalledTimes(1);
      });
  });

  it("should getAll an action to add a todo", async () => {
    const monthPayment = { id: 1, projectId: 1, rate: 500 };
    const expectedAction = {
      type: monthPaymentActionTypes.REMOVE,
      monthPaymentId: monthPayment.id
    };
    monthPaymentService.remove.mockImplementationOnce(monthPaymentId => {
      return Promise.resolve(monthPaymentId);
    });

    const store = mockStore({});

    return store
      .dispatch(monthPaymentActions.remove(monthPayment.id))
      .then(() => {
        const action = store.getActions();
        expect(action.length).toBe(1);
        expect(action).toContainEqual(expectedAction);
        expect(monthPaymentService.remove).toHaveBeenCalledTimes(1);
      });
  });
});
