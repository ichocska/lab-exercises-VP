from entities import account
from entities import errors
class User():
    egn = []
    __users = []
    def __init__(self, egn: str, name) -> None:
        self.accounts = []
        if len(egn) != 10 or not egn.isnumeric():
            raise Exception('Invalid EGN')
        if name in self.__users:
            raise errors.UserAlreadyExists('This user is already present')
        self.egn = egn
        self.name = name
        self.__users.append(name)
    def __repr__(self) -> str:
        return f'User: {self.name} {self.egn}'
    