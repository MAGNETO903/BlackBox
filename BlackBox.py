import math
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
ORANGE = (255, 128, 0)

pygame.init()

def get_polygon(c_x, c_y, n):
    out = []
    step = math.pi*2/n
    for a in range(n):
        out.append([c_x+math.cos(step*a)*50, c_y+math.sin(a*step)*50])

    return out

class BlackBox:
    __instance = None

    def __init__(self):
        if not BlackBox.__instance:
            self.colors = [WHITE, BLACK, GRAY, RED, BLUE, LIGHT_BLUE, GREEN, YELLOW, PINK, ORANGE]

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

    def get_response(self, user_message):
        screen = pygame.Surface((500, 500))
        screen.fill((255, 255, 255))
        verts_num_1 = user_message[0]
        color_1 = user_message[1]
        dots_num_1 = user_message[2]

        verts_num_2 = user_message[3]
        color_2 = user_message[4]
        dots_num_2 = user_message[5]

        verts_num_3 = user_message[6]
        color_3 = user_message[7]
        dots_num_3 = user_message[8]

        if verts_num_1 in ['0', '9']:
            pygame.draw.circle(screen, self.colors[color_1], (100, 100), 50)
        else:
            pass


        pygame.image.save(screen, "pic.png")
        pygame.quit()
        return open('pic.png')
        


