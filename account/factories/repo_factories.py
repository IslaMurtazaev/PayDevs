from account.repositories import UserRepo



class UserRepoFactory(object):
    @staticmethod
    def create():
        return UserRepo()






