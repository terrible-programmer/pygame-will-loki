import pygame
import sys
import time
import numpy

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.music.load('soundfile.mp3')
pygame.mixer.music.play()

size = width,height = 1000,1000
speed = [2,2]
speed2 = [1,1]
white = (255, 255, 255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("BALLZ 2D.jpg");
ball2 = pygame.image.load("BALLZ 2D4.jpg")
ball3 = pygame.image.load("BALLZ 2D5.jpg")
ballrect = ball.get_rect()
print ball.get_rect()

ballrect2 = ball2.get_rect()
ballrect3 = ball3.get_rect()
ballrect = ballrect.move(0,0)
ballrect2 = ballrect2.move(140,0)
ballrect3 = ballrect3.move(280,0)
print ballrect2.size
lasttime = 0
lasttime2 = 0
lasttime3 = 0
x = time.time()
time.time() - x 

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			speed = [val + numpy.sign(val) for val in speed]
			print speed 
			#if speed[0] >=0:
				#print speed
			#if speed[0] < 0:
				#y = speed - (speed * 2)

			

	if (pygame.time.get_ticks() - lasttime > 1):
		ballrect = ballrect.move(speed)
		lasttime = pygame.time.get_ticks() #Update the timer so that it happens again in another 100 ticks

	if (pygame.time.get_ticks() - lasttime2 > 1):
		ballrect2 = ballrect2.move(speed)
		lasttime2 = pygame.time.get_ticks()

	if(pygame.time.get_ticks() - lasttime3 > 1):
		ballrect3 = ballrect3.move(speed)
		lasttime3 = pygame.time.get_ticks()

	if ballrect.left < 0 or ballrect.right > width:
			speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1]=-speed[1]
		
	if ballrect2.left < 0 or ballrect2.right > 861:
			speed2[0] = -speed2[0]
	if ballrect2.top < 0 or ballrect2.bottom > 858:
		speed2[1]=-speed2[1]
	print time.time() - x
	if (time.time() - x) > 30: 
		break
	
		

	screen.fill(white)
	screen.blit(ball,ballrect)
	screen.blit(ball2,ballrect2)
	screen.blit(ball3,ballrect3)	
	pygame.display.flip()