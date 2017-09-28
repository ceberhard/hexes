import pygame
import math

BLACK = (0, 0, 0, 0)
WHITE = (255, 255, 255, 255)

def main():
	screensize = [500, 500]
	screen = pygame.display.set_mode(screensize)
	pygame.display.set_caption('Testing 123')
	
	done = False
	clock = pygame.time.Clock()
	
	while not done:
		clock.tick(10)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
		screen.fill(WHITE)
		
		hexside = 20
		center = [250, 250]
		
		pts = []
		for i in range(1,7):
			pts.append(hexpoint(center, hexside, i))

#		pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
		pygame.draw.polygon(screen, BLACK, pts, 1)
		
		center = [center[0] + hexside * 1.5, center[1] + hexside]
		
		pts = []
		for i in range(1,7):
			pts.append(hexpoint(center, hexside, i))

		pygame.draw.polygon(screen, BLACK, pts, 1)
		
		pygame.display.flip()
		
	pygame.quit()


def hexpoint(center, size, cornerindex):
	angledeg = 60 * cornerindex
	anglerad = math.pi / 180 * angledeg
	return [center[0] + size * math.cos(anglerad), center[1] + size * math.sin(anglerad)]

if __name__ == '__main__':
	main()
