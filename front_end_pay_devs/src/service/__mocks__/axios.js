export default {
    
    get: jest.fn((url) => {
        return Promise.resolve({
            data: {}
        });
    
    }),
    post: jest.fn((url, data) => {
        var parser = document.createElement('a');
        parser.href = url;
        let pathList = parser.pathname.split("/")
        
        // let urlList = url.split('/')
        if(pathList.indexOf('users') !== -1){
            return userAxiosRender(pathList, data);
        }
        let user = JSON.parse(data)
        return Promise.resolve({ data: {username: user.username, password: user.password} })
          
    }),
    create: jest.fn(function () {
        return this;
    }),
    defaults: jest.fn((url) => {
        return Promise.resolve({
            data: {}
        });
    
    }),

    
};

function userAxiosRender(pathList, data){
    const user = JSON.parse(data)
    const path = pathList.pop()
    if(path === 'login'){
        if(user.username === 'test_user_name' && user.username === 'test_user_name')
            return Promise.resolve({ data: {
                username: user.username, 
                email: 'test@gmail.com',
                token: "__TOKEN__"
            } })
        else{
            return Promise.resolve({ data: {error: {
                source: "entity",
                code: "not_found",
                message: "Entity not found"
            } }})
        }
    }else if (path === 'create'){
        return Promise.resolve({ data: {
            username: user.username, 
            email: user.email,
            token: "__TOKEN__"
        } })
    }
}