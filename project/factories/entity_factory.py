from project.entities import Project, WorkTask, MonthPayment, WorkedDay, HourPayment, WorkTime


class ProjectEntityFactory:
    @staticmethod
    def create():
        return ProjectEntity


class ProjectEntity:
    @staticmethod
    def create(**kwargs):
        return Project(**kwargs)



class WorkTaskEntityFactory:
    @staticmethod
    def create():
        return WorkTaskEntity


class WorkTaskEntity:
    @staticmethod
    def create(**kwargs):
        return WorkTask(**kwargs)



class MonthPaymentEntityFactory:
    @staticmethod
    def create():
        return MonthPaymentEntity


class MonthPaymentEntity:
    @staticmethod
    def create(**kwargs):
        return MonthPayment(**kwargs)



class WorkedDayEntityFactory:
    @staticmethod
    def create():
        return WorkedDayEntity


class WorkedDayEntity:
    @staticmethod
    def create(**kwargs):
        return WorkedDay(**kwargs)



class HourPaymentEntityFactory:
    @staticmethod
    def create():
        return HourPaymentEntity


class HourPaymentEntity:
    @staticmethod
    def create(**kwargs):
        return HourPayment(**kwargs)



class WorkTimeEntityFactory:
    @staticmethod
    def create():
        return WorkTimeEntity


class WorkTimeEntity:
    @staticmethod
    def create(**kwargs):
        return WorkTime(**kwargs)
