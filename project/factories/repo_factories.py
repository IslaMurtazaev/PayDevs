from project.repositories import ProjectRepo, WorkTaskRepo, WorkDayRepo, WorkTimeRepo


class ProjectRepoFactory(object):
    @staticmethod
    def create():
        return ProjectRepo()


class WorkTaskRepoFactory(object):
    @staticmethod
    def create():
        return WorkTaskRepo()


class WorkDayRepoFactory(object):
    @staticmethod
    def create():
        return WorkDayRepo()


class WorkTimeRepoFactory(object):
    @staticmethod
    def create():
        return WorkTimeRepo()
