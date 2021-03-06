class BlackBox:
    __instance = None

    def __init__(self):
        if not BlackBox.__instance:
            pass
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = BlackBox()
        return cls.__instance

    def make_transformation(self, user_try):
        if user_try.isdigit() == False:
            return 'Введите пожалуйста 9-значное число'
        elif len(user_try) != 9:
            return 'Пожалуйста, введите число, состоящее ровно из 9 цифр'
        else:
            return 'Пока не знаю, что ответить...'

    def get_greeting_message(self):
        return 'Здравствуйте!'