import {UserService} from '../service/user';
import {UserConstant} from '../constants/user';
import {history} from '../index'

export const userActions = {
    authentication,
    logout,
    sign_up
};


function authentication(username, password) {
    return dispatch=>{
            UserService.login(username, password).then((user) =>
                {
                    dispatch({type: UserConstant.LOGIN_USER, user});
                    history.push('projects');
                },
                error =>{
                    if(error.response)
                        dispatch({type: UserConstant.LOGIN_ERROR, error: error.response.data});
                    else
                        dispatch({type: UserConstant.LOGIN_ERROR, error: error});
                }    
          
            )
    }
    //  
}


function sign_up(username, email, password) {
    return dispatch=>{
            UserService.create_user(username, email, password).then((user) =>
                {
                    dispatch({type: UserConstant.LOGIN_USER, user});
                    history.push('projects');
                },
                error =>{
                    if(error.response)
                        dispatch({type: UserConstant.LOGIN_ERROR, error: error.response.data});
                    else
                        dispatch({type: UserConstant.LOGIN_ERROR, error: error});
                }    
          
            )
    }
    //  
}


function logout(){
    UserService.logout();
    return dispatch => {
        dispatch({type: UserConstant.LOGOUT})
    }
}

