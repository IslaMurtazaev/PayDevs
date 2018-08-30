export const taskService = {
    getAll: jest.fn((url) => {
        return Promise.resolve({
            data: {}
        });
    })
}