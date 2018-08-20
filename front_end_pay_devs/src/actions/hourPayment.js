import { hourPaymentService } from "../service/hourPayment";
import {HourPaymentConstant} from '../constants/hourPayment'
import {history} from '../index';

export const hourPaymentActions = {
    getAll,
    create,
    deleteHour,
    update
  };

function getAll(projectId) {
return dispatch => {
    hourPaymentService.getAll(projectId).then(hourPayments => {
        
    dispatch({ type: HourPaymentConstant.GET_ALL, hourPayments });
    });
};
}


function create(hourPayment) {
return dispatch => {
    hourPaymentService
    .create(hourPayment)
    .then(hourPayment => {
        dispatch({ type: HourPaymentConstant.CREATE, hourPayment });
        // history.push(`/project/${hourPayment.projectId}`)
        
    })
    .catch(error => {
        alert(error);
    });
};
}

function deleteHour(hourId) {
    return dispatch => {
        hourPaymentService.deleteHour(hourId).then(hourPayment => {
        dispatch({ type: HourPaymentConstant.DELETE, hourPayment});
      });
    };
  }


function update(values){
return dispatch => {
    hourPaymentService
        .update(values)
        .then(hourPayment => {
        dispatch({ type: HourPaymentConstant.CREATE, hourPayment });
        history.push(`/project/${values.projectId}`)
        })
        .catch(error => {
        alert(error);
        });
    }
}