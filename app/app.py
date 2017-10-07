import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

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
		
		# pts = []
		# for i in range(1,7):
		#	pts.append(hexpoint(center, hexside, i))

		# pygame.draw.polygon(screen, BLACK, pts, 1)
		drawhex(screen, center, hexside)

		adjsize = (hexside * 1.75)
		
		# testdeg = 90
		# testrad = math.radians(testdeg)
		# testpt = [center[0] + adjsize * math.cos(testrad), center[1] + adjsize * math.sin(testrad)]

		for i in range(1,7):
			testpt = hexpoint(center, adjsize, i, shift=30)
			pygame.draw.polygon(screen, RED, [center, testpt], 1)
			# pts = []
			# for i in range(1,7):
			# 	pts.append(hexpoint(testpt, hexside, i))
			# pygame.draw.polygon(screen, BLACK, pts, 1)
			drawhex(screen, testpt, hexside)
		
		
		# center = [center[0] + hexside * 1.5, center[1] + hexside]
		
		# pts = []
		# for i in range(1,7):
			# pts.append(hexpoint(center, hexside, i))

		# pygame.draw.polygon(screen, BLACK, pts, 1)
		
		pygame.display.flip()
		
	pygame.quit()

def drawhex(screen, center, sidelength):
	pts = []
	for i in range(1,7):
		pts.append(hexpoint(center, sidelength, i))
	pygame.draw.polygon(screen, BLACK, pts, 1)

def hexpoint(center, size, cornerindex, shift = 0):
	anglerad = math.radians((60 * cornerindex) + shift)
	return [center[0] + size * math.cos(anglerad), center[1] + size * math.sin(anglerad)]

if __name__ == '__main__':
	main()
