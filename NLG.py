class NLGMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class NLG(metaclass=NLGMeta):
    def __init__(self):
        pass

    def get_message(self, msg, user_status, nlu, special_info):
        if user_status == "GREETING":
            return "Здравствуйте!"
        elif user_status == "ANSWERING":
            msg_status = nlu.check_message(msg)
            # отправляем картинку
            if msg_status == 0:
                return special_info.pic
            elif msg_status == 1:
                # введите именно 9-значное число
                return "Пожалуйста введите код, состоящий ровно из 9 цифр"
            elif user_status == 2:
                # введите код, состоящий только из 9 цифр
                return "Введите код, состоящий только из 9 цифр"



