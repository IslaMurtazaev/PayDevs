import { workTimeService } from "../service/workTime";
import {WorkTimeConstant} from '../constants/workTime'
// import {history} from '../index';

export const workTimeActions = {
    create,
    getAll
};

function create(workTime) {
    return dispatch => {
        workTimeService
        .create(workTime)
        .then(workTime => {
            dispatch({ type: WorkTimeConstant.CREATE, workTime });
            
        })
        .catch(error => {
            alert(error);
        });
    };
}


function getAll(projectId, hourPaymentId) {
return dispatch => {
    workTimeService.getAll(projectId, hourPaymentId).then(workTimes => {
        dispatch({ type: WorkTimeConstant.GET_ALL, workTimes });
        });
    };
}