from account.repositories import UserRepo



class UserRepoFactory(object):
    @staticmethod
    def get():
        return UserRepo()






