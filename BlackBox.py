class BlackBox():
    def __init__(self):
        pass

    def make_transformation(self, user_try):
        if user_try.isdigit():
            return 'Введите пожалуйста 9-значное число'
        elif len(user_try) != 9:
            return 'Пожалуйста, введите число, состоящее ровно из 9 цифр'
        else:
            return 'Пока не знаю, что ответить...'

    def get_greeting_message(self):
        return 'Здравствуйте!'