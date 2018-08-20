import { workTimeService } from "../service/workTime";
import {WorkTimeConstant} from '../constants/workTime'
// import {history} from '../index';

export const workTimeActions = {
    create
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