from project.repositories import ProjectRepo, WorkTaskRepo, HourPaymentRepo, MonthPaymentRepo, WorkTimeRepo, \
    WorkedDayRepo


class ProjectRepoFactory(object):
    @staticmethod
    def create():
        return ProjectRepo()


class WorkTaskRepoFactory(object):
    @staticmethod
    def create():
        WorkTaskRepo()



class HourPaymentRepoFactory(object):
    @staticmethod
    def create():
        HourPaymentRepo()


class WorkTimeRepoFactory(object):

    @staticmethod
    def create():
        WorkTimeRepo()



class MonthPaymentRepoFactory(object):
    @staticmethod
    def create():
        MonthPaymentRepo()


class WorkedDayRepoFactory(object):
    @staticmethod
    def create():
        WorkedDayRepo()


