from project.repositories import ProjectRepo, WorkTaskRepo, HourPaymentRepo, MonthPaymentRepo, WorkTimeRepo, \
    WorkedDayRepo


class ProjectRepoFactory:
    @staticmethod
    def create():
        return ProjectRepo()


class WorkTaskRepoFactory:
    @staticmethod
    def create():
        return WorkTaskRepo()



class HourPaymentRepoFactory:
    @staticmethod
    def create():
        return HourPaymentRepo()


class WorkTimeRepoFactory:
    @staticmethod
    def create():
        return WorkTimeRepo()



class MonthPaymentRepoFactory:
    @staticmethod
    def create():
        return MonthPaymentRepo()


class WorkedDayRepoFactory:
    @staticmethod
    def create():
        return WorkedDayRepo()
