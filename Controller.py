class Controller():
    def __init__(self):
        self.users = dict()

    def add_user(self, user_id):
        self.users[user_id] = 'GREETING'