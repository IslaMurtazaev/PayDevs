from project.repositories import ProjectRepo, WorkTaskRepo, HourPaymentRepo, MonthPaymentRepo, WorkTimeRepo, \
    WorkedDayRepo


class ProjectRepoFactory(object):
    @staticmethod
    def create():
        return ProjectRepo()


class WorkTaskRepoFactory(object):
    @staticmethod
    def create():
        return WorkTaskRepo()



class HourPaymentRepoFactory(object):
    @staticmethod
    def create():
        return HourPaymentRepo()


class WorkTimeRepoFactory(object):
    @staticmethod
    def create():
        return WorkTimeRepo()



class MonthPaymentRepoFactory(object):
    @staticmethod
    def create():
        return MonthPaymentRepo()


class WorkedDayRepoFactory(object):
    @staticmethod
    def create():
        return WorkedDayRepo()
