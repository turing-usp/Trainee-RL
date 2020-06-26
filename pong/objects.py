import pygame
import numpy as np  


class Bar:
    def __init__(self, x, y, screen_width, screen_height, length=20, width=2, velocity=2, orientation=1):
        self.x = int(x)
        self.y = int(y)
        self.length = length
        self.width = width
        self.velocity = velocity
        self.orientation = orientation  # 1 para horizontal, 0 para vertical
        self.screen_width = screen_width
        self.screen_height = screen_height

    def draw(self, screen, color=(255, 255, 255)):  # desenhar em pygame
        pygame.draw.rect(screen, color, [
                         self.x-self.width/2, self.y-self.length/2, self.width, self.length])

    # mode = (human, machine, enemy); move = (0,1,2)
    def move(self, mode='human', move=None, ball=None):
        lookup_table = {pygame.K_s: lambda x: x + self.velocity,
                        1: lambda x: x + self.velocity,  # movimentamos a barra verticalmente
                        pygame.K_w: lambda x: x - self.velocity,
                        2: lambda x: x - self.velocity}  # conforme a tabela indica

        # modos de movimento: o mode 'human' serve para o controle manual,
        # 'machine' diz respeito ao environment e o 'enemy' serve para controlar
        # a barra inimiga
        if mode == 'human':
            pressed = pygame.key.get_pressed()
            for k in lookup_table.keys():  # verificamos se a tecla foi apertada
                if pressed[k]:
                    self.y = lookup_table[k](self.y)
            # clamping
            if self.y >= self.screen_height:
                self.y = self.screen_height
            elif self.y <= 0:
                self.y = 0

        elif mode == 'machine':
            if move != 0:
                self.y = lookup_table[move](self.y)
            # clamp
            if self.y >= self.screen_height:
                self.y = self.screen_height
            elif self.y <= 0:
                self.y = 0

        elif mode == 'enemy':
            if self.y != ball.y and np.random.random() < .6 and ball.x >= self.screen_width*.8:
                vec = ((ball.y - self.y)/abs(ball.y - self.y))
            else:
                vec = 0
            self.y += self.velocity*vec


class Ball:
    def __init__(self, x, y, radius, velocity=1):
        self.x = int(x)
        self.y = int(y)
        self.radius = radius
        self.abs_velocity = velocity
        self.reset_velocity()

    def reset_velocity(self):
        v = self.abs_velocity
        direction = np.random.uniform(np.pi/8, np.pi/3)  # first quadrant
        direction *= np.random.choice([-1, 1])  # right side
        direction += np.random.choice([0, np.pi])  # left sideu
        self.velocity = [
            v*np.cos(direction), -v*np.sin(direction)]

    def move(self):
        self.x = self.x + self.velocity[0]
        self.y = self.y + self.velocity[1]

    def draw(self, screen, color=(255, 255, 255)):
        pygame.draw.circle(
            screen, color, [int(self.x), int(self.y)], self.radius)

    def bounce(self, wall):
        lookup_table = {0: [-1, 1],
                        1: [1, -1]}
        if abs(self.x - wall.x) <= wall.width/2 and abs(self.y - wall.y) <= wall.length/2:
            self.velocity[0] *= lookup_table[wall.orientation][0]
            self.velocity[1] *= lookup_table[wall.orientation][1]


class Environment:
    def __init__(self, HEIGHT=300, WIDTH=400, easy_mode=True,
                 bar_velocity=6, ball_velocity=2, matches=7, max_steps=10_000, fps=100):
        # x, y, length, width, velocity, orientation
        bar_parameters = [(15, HEIGHT/2, 100, 5, bar_velocity, 0),
                          (WIDTH-15, HEIGHT/2, 100, 5, bar_velocity, 0),
                          (WIDTH/2, 0,  2, WIDTH, 0, 1),
                          (WIDTH / 2, HEIGHT,  2, WIDTH, 0, 1),
                          (0, HEIGHT/2, HEIGHT, 2, 0, 0),
                          (WIDTH, HEIGHT/2, HEIGHT, 2, 0, 0)]

        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.max_steps = max_steps
        self.rendered = False
        self.matches = matches
        self.easy_mode = easy_mode
        self.fps = fps
        self.clock = pygame.time.Clock()

        self.bars = []
        for x, y, length, width, velocity, orientation in bar_parameters:
            self.bars.append(Bar(x, y, WIDTH, HEIGHT, length,
                                 width, velocity, orientation))
        self.control_bar = self.bars[0]
        self.other_bar = self.bars[1]

        # x inicial; y inicial; raio
        self.ball = Ball(WIDTH/2, HEIGHT/2, 10, ball_velocity)

    def reset(self):
        self.ball.x, self.ball.y = self.WIDTH/2, self.HEIGHT/2
        self.steps = 0
        self.control_bar.x, self.control_bar.y = 15, self.HEIGHT/2
        self.other_bar.x, self.other_bar.y = self.WIDTH - 15, self.HEIGHT/2
        self.ball.reset_velocity()
        self.done = False
        self.score = [0, 0]

        dx = self.control_bar.x - self.ball.x
        dy = self.control_bar.y - self.ball.y

        return ((dx, dy))

    def step(self, action):
        reward = 0
        self.steps += 1
        self.control_bar.move(mode='machine', move=action)
        self.other_bar.move(mode='enemy', ball=self.ball)
        self.ball.move()

        for bar in self.bars:
            self.ball.bounce(bar)

        if self.ball.x <= 4:

            self.ball.x, self.ball.y = self.WIDTH/2, self.HEIGHT/2
            self.control_bar.x, self.control_bar.y = 15, self.HEIGHT/2
            self.other_bar.x, self.other_bar.y = self.WIDTH - 15, self.HEIGHT/2
            self.ball.reset_velocity()

            self.score[1] += 1
            reward = -500
            if self.score[-1] >= self.matches / 2:
                self.done = True
                reward -= 2000

        elif self.ball.x >= self.WIDTH - 4:

            self.ball.x, self.ball.y = self.WIDTH/2, self.HEIGHT/2
            self.control_bar.x, self.control_bar.y = 15, self.HEIGHT/2
            self.other_bar.x, self.other_bar.y = self.WIDTH - 15, self.HEIGHT/2
            self.ball.reset_velocity()

            self.score[0] += 1
            reward = +500
            if self.score[0] >= self.matches/2:
                self.done = True
                reward += 2000

        if self.steps >= self.max_steps:
            self.done = True

        if self.easy_mode:
            dx = self.control_bar.x - self.ball.x
            dy = self.control_bar.y - self.ball.y
            state = np.array([dx, dy])
        else:
            state = np.array([self.control_bar.x, self.control_bar.y,
                              self.ball.x, self.ball.y])

        return (state, reward, self.done, {})

    def render(self, wait=True):
        if not self.rendered:
            self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            self.rendered = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        self.screen.fill((100, 100, 100))
        for bar in self.bars:
            bar.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.update()
        if wait:
            self.clock.tick(self.fps)
