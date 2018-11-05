export const taskService = {
    getAll: jest.fn(() => {
        return Promise.resolve({
            tasks: {}
        });
    }),
    create: jest.fn(() => {
        return Promise.resolve({
            tasks: {}
        });
    }),
    update: jest.fn(() => {
        return Promise.resolve({
            task: {}
        });
    }),
    remove: jest.fn(() => {
        return Promise.resolve({
            taskId: {}
        });
    })
}