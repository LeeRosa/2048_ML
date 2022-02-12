import pygame
import sys         # ❶ 파이게임 모듈 임포트하기
import time
import numpy
import numpy as np
import math
import random
from random import randint
import copy
import gym_2048
import gym

pygame.init()              # ❸ 파이게임을 사용하기 전에 초기화한다.

move = 0
Screen = pygame.display.set_mode((600,750))
pygame.display.set_caption('2048')
finish = False
colorBlue = True
x = 60
y = 60
clock = pygame.time.Clock()
Score = 0
Size = 4  # 4*4行列
Block_WH = 110  # 블럭의 길이 폭
BLock_Space = 10  # 블럭사이 간격
score = 0
Block_Size = Block_WH * Size + (Size + 1) * BLock_Space
Matrix = numpy.zeros([Size, Size])  # 초기화 행렬 4x4의 0행렬
Screen_Size = (Block_Size, Block_Size + 110)
boxsize = min(530, 530) // 4;
colorback = (189, 174, 158)
colorblank = (205, 193, 180)
colorlight = (249, 246, 242)
colordark = (119, 110, 101)
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
TABLE = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Color = {
    0: (205,193,180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 95, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    4096: (237, 190, 30),
    8192: (239, 180, 25)}
Color2 = {
    2: colordark,
    4: colordark,
    8: colorlight,
    16: colorlight,
    32: colorlight,
    64: colorlight,
    128: colorlight,
    256: colorlight,
    512: colorlight,
    1024: colorlight,
    2048: colorlight,
    4096: colorlight,
    8192: colorlight
}


class game:

    def __init__(self):
        self.daback = 0
        self.action_space = [1, 2, 3, 4]
        #self.n_actions = len(self.action_space)
        self.score = 0
        self.bestscore = 0

    def show(self,TABLE):
        # showing the table
        for i in range(4):
            for j in range(4):
                pygame.draw.rect(Screen, Color[TABLE[i][j]], pygame.Rect(j * boxsize + 43,
                                                                   i * boxsize + 200,
                                                                   boxsize - 2 * 10,
                                                                   boxsize - 2 * 10),
                                 0)
                if TABLE[i][j] != 0:
                    order = int(math.log10(TABLE[i][j]))
                    myfont = pygame.font.SysFont("Arial", order+70 , bold=True)
                    label = myfont.render("%4s" % (TABLE[i][j]), 1, Color2[TABLE[i][j]])
                    Screen.blit(label, (j * boxsize + 7 * 5, i * boxsize + 42 * 5))

        game.updatascore(0)

        pygame.display.update()

    def randomfill(self,TABLE):
        # search for zero in the game table and randomly fill the places
        flatTABLE = sum(TABLE, [])
        if 0 not in flatTABLE:
            return TABLE
        empty = False
        w = 0
        while not empty:
            w = randint(0, 15)
            if TABLE[w // 4][w % 4] == 0:
                empty = True
        z = randint(1, 5)
        if z == 5:
            TABLE[w // 4][w % 4] = 4
        else:
            TABLE[w // 4][w % 4] = 2
        return TABLE

    def reset(self):
        TABLE = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.show(TABLE)
        self.randomaction(TABLE)
        return TABLE

    def gameOver(self, TABLE):
        # returns False if a box is empty or two boxes can be merged
        x = [-1, 0, 1, 0]
        y = [0, 1, 0, -1]
        for pi in range(4):
            for pj in range(4):
                if TABLE[pi][pj] == 0:
                    return False
                for point in range(4):
                    if pi + x[point] > -1 and pi + x[point] < 4 and pj + y[point] > -1 and pj + y[point] < 4 and TABLE[pi][
                        pj] == TABLE[pi + x[point]][pj + y[point]]:
                        return False
        return True

    def showGameOverMessage(self):
        # to show game over screen
        titleFont = pygame.font.Font('freesansbold.ttf', 60)
        titleSurf1 = titleFont.render('Game Over', True, (255, 255, 255), (0, 0, 0))

        '''rrruning = True
        while rrruning:'''
        display_rect = pygame.transform.rotate(titleSurf1, 0)
        rectangle = display_rect.get_rect()
        rectangle.center = (300 , 500)
        Screen.blit(display_rect, rectangle)
        #self.runGame(TABLE)
        pygame.display.update()




    def runGame(self, TABLE):
        #TABLE = randomfill(TABLE)
        TABLE = self.randomfill(TABLE)
        self.show(TABLE)
        running = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if running:
                        desired_key = None
                        if event.key == pygame.K_UP: desired_key = 1
                        if event.key == pygame.K_DOWN: desired_key = 2
                        if event.key == pygame.K_LEFT: desired_key = 3
                        if event.key == pygame.K_RIGHT: desired_key = 4
                        if desired_key is None:
                            continue

                        new_table = self.key(desired_key, copy.deepcopy(TABLE))
                        if new_table != TABLE:
                            TABLE = self.randomfill(new_table)
                            self.show(TABLE)
                        if self.gameOver(TABLE):
                            self.score = 0
                            self.showGameOverMessage()
                            self.show(TABLE)

                if event.type == pygame.QUIT:  # 끝났으면
                    finish = True
                    pygame.quit()  # pygame을 종료한 후
                    sys.exit()  # 프로그램 종료

    def runGame1(self, TABLE):  #랜덤플레이
        #TABLE = randomfill(TABLE)
        TABLE = self.randomfill(TABLE)
        self.show(TABLE)
        running = True
        while running:
            game.randomaction(TABLE)
            TABLE = self.randomfill(TABLE)
            self.show(TABLE)

            if self.gameOver(TABLE):
                self.score = 0
                self.showGameOverMessage()
                running = False
                #pygame.display.flip()  # 디스플레이 업데이트
        TABLE = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.show(TABLE)
        self.runGame1(TABLE)



    def key(self, DIRECTION, TABLE):
        if DIRECTION == 0:
            for pi in range(1, 4):
                for pj in range(4):
                    if TABLE[pi][pj] != 1: TABLE = self.moveup(pi, pj, TABLE)
        elif DIRECTION == 1:
            for pi in range(2, -1, -1):
                for pj in range(4):
                    if TABLE[pi][pj] != 2: TABLE = self.movedown(pi, pj, TABLE)
        elif DIRECTION == 2:
            for pj in range(1, 4):
                for pi in range(4):
                    if TABLE[pi][pj] != 3: TABLE = self.moveleft(pi, pj, TABLE)
        elif DIRECTION == 3:
            for pj in range(2, -1, -1):
                for pi in range(4):
                    if TABLE[pi][pj] != 4: TABLE = self.moveright(pi, pj, TABLE)
        return TABLE

    def randomaction(self, TABLE):
        x =  random.randrange(0,4)
        self.key(x,TABLE)
        return TABLE

    def movedown(self, pi, pj, T):
        justcomb = False
        while pi < 3 and (T[pi + 1][pj] == 0 or (T[pi + 1][pj] == T[pi][pj] and not justcomb)):
            if T[pi + 1][pj] == 0:
                T[pi + 1][pj] = T[pi][pj]
            elif T[pi + 1][pj] == T[pi][pj]:
                T[pi + 1][pj] += T[pi][pj]
                justcomb = True
                if T[pi + 1][pj] == 4:
                    self.score += 20
                if T[pi + 1][pj] == 8:
                    self.score += 40
                if T[pi + 1][pj] == 16:
                    self.score += 60
                if T[pi + 1][pj] == 32:
                    self.score += 80
                if T[pi + 1][pj] == 64:
                    self.score += 100
                if T[pi + 1][pj] == 128:
                    self.score += 120
                if T[pi + 1][pj] == 256:
                    self.score += 80
                if T[pi + 1][pj] == 512:
                    self.score += 100
                if T[pi + 1][pj] == 1024:
                    self.score += 120
                if T[pi + 1][pj] == 2048:
                    self.score += 200
            T[pi][pj] = 0
            pi += 1
        return T


    def moveleft(self, pi, pj, T):
        justcomb = False
        while pj > 0 and (T[pi][pj - 1] == 0 or (T[pi][pj - 1] == T[pi][pj] and not justcomb)):
            if T[pi][pj - 1] == 0:
                T[pi][pj - 1] = T[pi][pj]
            elif T[pi][pj - 1] == T[pi][pj]:
                T[pi][pj - 1] += T[pi][pj]
                if T[pi][pj - 1] == 4:
                    self.score += 20
                if T[pi][pj - 1] == 8:
                    self.score += 40
                if T[pi][pj - 1] == 16:
                    self.score += 60
                if T[pi][pj - 1] == 32:
                    self.score += 80
                if T[pi][pj - 1] == 64:
                    self.score += 100
                if T[pi][pj - 1] == 128:
                    self.score += 120
                if T[pi][pj - 1] == 256:
                    self.score += 80
                if T[pi][pj - 1] == 512:
                     self.score += 100
                if T[pi][pj - 1] == 1024:
                     self.score += 120
                if T[pi][pj - 1] == 2048:
                     self.score += 200
                     self.daback += 1
                justcomb = True
            T[pi][pj] = 0
            pj -= 1
        return T


    def updatascore(self, score):
        self.score += score
        if self.score > self.bestscore:
            self.bestscore = self.score
        game.writescore()

    def reward(self, score):
        if score == 0:
            reward = 0
            done = False
        elif score == 20:
            reward = 10
            done = True
        elif score == 40:
            reward = 20
            done = True
        elif score == 60:
            reward = 30
            done = True
        elif score == 80:
            reward = 40
            done = True
        elif score == 100:
            reward = 50
            done = True
        elif score == 120:
            reward = 60
            done = True
        return TABLE,reward, done,

    def moveright(self, pi, pj, T):
        justcomb = False
        while pj < 3 and (T[pi][pj + 1] == 0 or (T[pi][pj + 1] == T[pi][pj] and not justcomb)):
            if T[pi][pj + 1] == 0:
                T[pi][pj + 1] = T[pi][pj]
            elif T[pi][pj + 1] == T[pi][pj]:
                T[pi][pj + 1] += T[pi][pj]
                justcomb = True
                if T[pi][pj + 1] == 4:
                    self.score += 20
                if T[pi][pj + 1] == 8:
                    self.score += 40
                if T[pi][pj + 1] == 16:
                    self.score += 60
                if T[pi][pj + 1] == 32:
                    self.score += 80
                if T[pi][pj + 1] == 64:
                    self.score += 100
                if T[pi][pj + 1] == 128:
                    self.score += 120
                if T[pi][pj + 1] == 256:
                    self.score += 80
                if T[pi][pj + 1] == 512:
                     self.score += 100
                if T[pi][pj + 1] == 1024:
                     self.score += 120
                if T[pi][pj + 1] == 2048:
                     self.score += 200
            T[pi][pj] = 0
            pj += 1
        return T


    def moveup(self, pi, pj, T):
        justcomb = False
        while pi > 0 and (T[pi - 1][pj] == 0 or (T[pi - 1][pj] == T[pi][pj] and not justcomb)):
            if T[pi - 1][pj] == 0:
                T[pi - 1][pj] = T[pi][pj]
            elif T[pi - 1][pj] == T[pi][pj]:
                T[pi - 1][pj] += T[pi][pj]
                justcomb = True
                if T[pi - 1][pj] == 4:
                    self.score += 20
                if T[pi - 1][pj] == 8:
                    self.score += 40
                if T[pi - 1][pj] == 16:
                    self.score += 60
                if T[pi - 1][pj] == 32:
                    self.score += 80
                if T[pi - 1][pj] == 64:
                    self.score += 100
                if T[pi - 1][pj] == 128:
                    self.score += 120
                if T[pi - 1][pj] == 256:
                    self.score += 80
                if T[pi - 1][pj] == 512:
                     self.score += 100
                if T[pi - 1][pj] == 1024:
                     self.score += 120
                if T[pi - 1][pj] == 2048:
                     self.score += 200
            T[pi][pj] = 0
            pi -= 1
        return T

    def writeMessage(self, text, size, position):
        font = pygame.font.Font('SDSwaggerTTF.ttf', size) #폰트 설정
        text = font.render(text,True,(90,80,50))  #텍스트가 표시된 Surface 를 만듬
        textt = text.get_rect()
        textt.center = position
        Screen.blit(text,textt)             #화면에 표시

    def writescore(self):
        pygame.draw.rect(Screen, (250,248,239), pygame.Rect(325, 68, 230, 100))
        game.writeMessage('2048 : %d' % (game.daback), 30, (485, 45))
        game.writeMessage('SCORE : %d' %(self.score), 30, (485, 115))
        game.writeMessage('BEST SCORE : %d' %(self.bestscore), 30, (460, 155))
        game.writeMessage('TIME : %f' %(time.time() - endTime), 30, (466, 83))


def Q_learning(TABLE):
    if __name__ == '__main__':
      env = gym.make('2048-v0')
      env.seed(30)
      env.reset()
      env.render()
      done = False
      moves = 0


      game.show(TABLE)

      TABLE = game.randomfill(TABLE)
      game.show(TABLE)
      #TABLE = game.randomfill(TABLE)


      while not done:
        gym_2048.Base2048Env.board = TABLE
        game.show(gym_2048.Base2048Env.board)
        action = env.np_random.choice(range(4), 1).item()
        game.key(action, gym_2048.Base2048Env.board)
        game.randomfill(gym_2048.Base2048Env.board)
        next_state, reward, done, info = env.step(action)
        moves += 1
        game.show(gym_2048.Base2048Env.board)
        pygame.draw.rect(Screen, (250, 248, 239), pygame.Rect(300, 10, 280, 100)) #248, 239
        game.writeMessage('moves : %d' %(moves), 30, (370, 33))

        print('Next Action: "{}"\n\nReward: {}'.format(
        gym_2048.Base2048Env.ACTION_STRING[action], reward))
        env.render()


        if game.gameOver(gym_2048.Base2048Env.board):
            game.score = 0
            #game.showGameOverMessage()
            #pygame.display.flip()  # 디스플레이 업데이트
            TABLE = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            game.show(gym_2048.Base2048Env.board)


    print('\nTotal Moves: {}'.format(moves))

while not finish:

    Screen.fill((250,248,239))
    endTime = time.time()
    game: game = game()
    game.writeMessage('2048-AI', 90, (155,70))
    pygame.draw.rect(Screen, (186,172,159), pygame.Rect(20, 178, 555, 555))
    game.writeMessage('Join the numbers and get to the 2048 tile!', 17, (150,137))
    game.writeMessage('Or watch the randomizing AI attempt to solve it!', 17, (170,160))

    print(endTime)
    Q_learning(TABLE)
    #game.runGame1(TABLE)
    pygame.display.flip()   #디스플레이 업데이트



