export const UserService = {
    login: jest.fn(() =>
        Promise.resolve({
            user: {}
        })
    ),
    create_user: jest.fn(() =>
        Promise.resolve({
            user: {}
        })
    ),
    logout: jest.fn(() =>
        Promise.resolve({
            user: {}
        })
    )
}