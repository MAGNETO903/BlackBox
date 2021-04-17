class NLUMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]



class NLU(metaclass=NLUMeta):
    def __init__(self):
        pass

    def check_message(self, msg):
        if msg.innumberic():
            if (len(msg) != 9):
                return 1
            else:
                return 0
        else:
            return 2