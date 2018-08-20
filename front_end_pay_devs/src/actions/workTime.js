import { workTimeService } from "../service/workTime";
import {workTimeConstant} from '../constants/workTime'
// import {history} from '../index';

export const workTimeActions = {
    create,
    getAll,
    deleteWork
};

function create(workTime) {
    return dispatch => {
        workTimeService
        .create(workTime)
        .then(workTime => {
            dispatch({ type: workTimeConstant.CREATE, workTime });
            
        })
        .catch(error => {
            alert(error);
        });
    };
}


function getAll(hourPaymentId) {
return dispatch => {
    workTimeService.getAll(hourPaymentId).then(workTimes => {
        dispatch({ type: workTimeConstant.GET_ALL, workTimes });
        });
    };
}

function deleteWork(workId) {
    return dispatch => {
        workTimeService.deleteWork(workId).then(workTime => {
        dispatch({ type: workTimeConstant.DELETE, workTime});
      });
    };
  }