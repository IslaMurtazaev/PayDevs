export default {
    getAll: jest.fn(() => {
        return Promise.resolve({
            workedDays: {}
        });
    }),
    create: jest.fn(() => {
        return Promise.resolve({
            workedDay: {}
        });
    }),
    update: jest.fn(() => {
        return Promise.resolve({
            workedDay: {}
        });
    }),
    remove: jest.fn(() => {
        return Promise.resolve({
            workedDayId: {}
        });
    })
}