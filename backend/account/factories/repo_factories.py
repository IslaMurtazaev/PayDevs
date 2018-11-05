from account.repositories import UserRepo

class UserRepoFactory:
    @staticmethod
    def create():
        return UserRepo()
