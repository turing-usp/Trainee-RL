import pygame
from objects import *

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bar_parameters = [(15,50,100,5,2,0),(WIDTH-15,50,100,5,3,0),
				  (WIDTH/2,0,2,WIDTH,0,1),(WIDTH/2,HEIGHT,2,WIDTH,0,1),
				  (0,HEIGHT/2,HEIGHT,2,0,0),(WIDTH,HEIGHT/2,HEIGHT,2,0,0)]

bars = []
for bar in bar_parameters:
	bars.append(Bar(bar[0],bar[1],bar[2],bar[3], bar[4], bar[5]))
control_bar = bars[0]
other_bar = bars[1]

ball = Ball(WIDTH/2,HEIGHT/2,10) #x inicial; y inicial; raio

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((100,100,100))

	for bar in bars:
		bar.draw(screen)
		ball.bounce(bar)
	ball.draw(screen)
	ball.move()
	control_bar.move()
	other_bar.move(mode='enemy',ball=ball)

	pygame.display.update()




