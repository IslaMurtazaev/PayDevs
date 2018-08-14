import {UserConstant} from '../constants/user'

let user_ = JSON.parse(localStorage.getItem('user'));
const initialState = user_ ? { loggedIn: true, user: user_ } : {};

export default function user(state=initialState, action){
    if (action.type === UserConstant.LOGIN_USER){
      return {
        user: action.user
      }
    
    }
    else if (action.type === UserConstant.LOGIN_ERROR){
      return {
        error: action.error
        
      }
    }
    return state;
  
  }