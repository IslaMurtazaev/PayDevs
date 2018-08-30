import configureStore from "redux-mock-store";
import thunk from "redux-thunk";

import { hourPaymentActions } from "../hourPayment";
import { hourPaymentActionTypes } from "../../constants/hourPayment";
import { hourPaymentService } from "../../service/hourPayment";
jest.mock("../../service/hourPayment.js");

const middlewares = [thunk];
const mockStore = configureStore(middlewares);
const store = mockStore({ hourPayments: [] });

describe("hourPayment's action creators", () => {
  afterEach(() => {
    store.clearActions()
  })

  it("creates ADD_ALL_HOUR_PAYMENTS action after fetching is done", () => {
    const fetchedHourPayments = [
      {
        id: 1,
        rate: 15
      },
      {
        id: 2,
        rate: 25
      }
    ];

    hourPaymentService.getAll.mockReturnValue(
      Promise.resolve(fetchedHourPayments)
    );

    const expectedActions = [
      {
        type: hourPaymentActionTypes.ADD_ALL,
        hourPayments: fetchedHourPayments
      }
    ];

    return store.dispatch(hourPaymentActions.getAll(1)).then(() => {
      expect(hourPaymentService.getAll).toHaveBeenCalled();
      expect(hourPaymentService.getAll).toBeCalledWith(1);
      expect(store.getActions()).toEqual(expectedActions);
    });
  });

  it("creates CREATE_HOUR_PAYMENT action after new hourPayment is created", () => {
    const createdHourPayment = [
      {
        rate: 15
      }
    ];

    hourPaymentService.create.mockReturnValue(
      Promise.resolve(createdHourPayment)
    );

    const expectedActions = [
      {
        type: hourPaymentActionTypes.CREATE,
        hourPayment: createdHourPayment
      }
    ];

    return store.dispatch(hourPaymentActions.create(createdHourPayment)).then(() => {
      expect(hourPaymentService.create).toHaveBeenCalled();
      expect(hourPaymentService.create).toBeCalledWith(createdHourPayment);
      expect(store.getActions()).toEqual(expectedActions);
    });
  });

  it("creates REMOVE_HOUR_PAYMENT action after removing hourPayment", () => {
    const removedHourPaymentId = 1;

    hourPaymentService.remove.mockReturnValue(
      Promise.resolve(removedHourPaymentId)
    );

    const expectedActions = [
      {
        type: hourPaymentActionTypes.REMOVE,
        hourPaymentId: removedHourPaymentId
      }
    ];

    return store.dispatch(hourPaymentActions.remove(removedHourPaymentId)).then(() => {
      expect(hourPaymentService.remove).toHaveBeenCalled();
      expect(hourPaymentService.remove).toBeCalledWith(removedHourPaymentId);
      expect(store.getActions()).toEqual(expectedActions);
    });
  });
});
