export default {
    getAll: jest.fn(() => {
        return Promise.resolve({
            monthPayments: {}
        });
    }),
    create: jest.fn(() => {
        return Promise.resolve({
            monthPayment: {}
        });
    }),
    update: jest.fn(() => {
        return Promise.resolve({
            monthPayment: {}
        });
    }),
    remove: jest.fn(() => {
        return Promise.resolve({
            monthPaymentId: {}
        });
    })
}