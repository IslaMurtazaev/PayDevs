from project.repositories import ProjectRepo, WorkTaskRepo, WorkDayRepo, WorkTimeRepo
from project.views import ProjectView, CreateProjectView, GetAllProjectsView, TotalView, CreateTaskView, \
            GetAllTasksView, UpdateProjectView, GetTaskView, UpdateTaskView, DeleteProjectView, DeleteTaskView, \
            CreateWorkDayView, CreateWorkTimeView, GetWorkDayView, GetWorkTimeView, UpdateWorkDayView, UpdateWorkTimeView, \
            DeleteWorkDayView, DeleteWorkTimeView, GetAllWorkDaysView, GetWorkTimeListView
from project.interactors import GetProjectInteractor, CreateProjectInteractor, GetAllProjectsInteractor, GetWorkedInteractor,\
            GetTotalInteractor, GetBillInteractor, CreateTaskInteractor, GetAllTasksInteractor, UpdateProjectInteractor, \
            GetTaskInteractor, UpdateTaskInteractor, DeleteProjectInteractor, DeleteTaskInteractor, CreateWorkDayInteractor, \
            CreateWorkTimeInteractor, GetWorkDayInteractor, GetWorkTimeInteractor, UpdateWorkDayInteractor, \
            UpdateWorkTimeInteractor, DeleteWorkDayInteractor, DeleteWorkTimeInteractor, GetTypeOfPaymentInteractor, \
            GetAllWorkDaysInteractor, GetWorkTimeListInteractor, GetTimestampInteractor
                                 


