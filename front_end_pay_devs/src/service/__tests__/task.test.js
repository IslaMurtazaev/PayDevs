jest.mock("../__mocks__/axios")

import {taskService} from '../task'

describe('Task', async () => {
    it('test function getAll', async () => {
        const data =  await taskService.getAll(1);
        console.log(data)
    })

})