// jest.mock("../axios")
// import mockAxios from "axios"

import {UserService} from "../user";
jest.mock("../helpers", () => require("helpers"))

describe('User sevice  ', () => {
    describe('Login User', () => {
        it('login user', async () => {
            const username = 'test_user_name';
            const passworrd = 'qwert12345'
            const data =  await UserService.login(username, passworrd);
            expect(data.username).toEqual(username);
            expect(data.email).toEqual('test@gmail.com');
            expect(data.token).toEqual('__TOKEN__');
        });
        it('login error', async () => {
            const username = 'test_user_name2';
            const passworrd = 'qwert12345'
            const data =  await UserService.login(username, passworrd);
          
            expect(data.error.source).toEqual('entity');
            expect(data.error.code).toEqual('not_found');
            expect(data.error.message).toEqual('Entity not found');
        });
    });
    describe('create User', () => {
        it('create user user', async () => {
            const username = 'test_user_name_two';
            const passworrd = 'qwert12345'
            const email = "test_creat_user@mail.com"
            
            const data =  await UserService.create_user(username, email, passworrd);
            
            expect(data.username).toEqual(username)
            expect(data.email).toEqual(email)
            expect(data.token).toEqual("__TOKEN__")
        });
    })

    describe('Logout User', () => {
        it('Logout', async () => {
            const username = 'test_user_name';
            const passworrd = 'qwert12345'
            const data =  await UserService.login(username, passworrd);
            let user = localStorage.getItem('user')
            expect(JSON.parse(user)).toEqual(data)
            UserService.logout()
            let userLogout = localStorage.getItem('user')
            expect(userLogout).toBeNull();
            
        });
    })
  });

//   .then(data =>{
//     console.log(data)
// }, error => {console.log(error)});