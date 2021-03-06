class Controller:
    __instance = None

    def __init__(self):
        if not Controller.__instance:
            self.users = dict()
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Controller()
        return cls.__instance

    def add_user(self, user_id):
        self.users[user_id] = 'GREETING'