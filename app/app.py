import pygame
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

hexgrid = []

def main():
	screensize = [500, 500]
	
	hexside = 20
	center = [hexside, hexside * 0.75]
	
	screen = pygame.display.set_mode(screensize)
	pygame.display.set_caption('Testing 123')
	
	done = False
	clock = pygame.time.Clock()
	
	pygame.init()
	
	while not done:
		clock.tick(10)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
				
		screen.fill(WHITE)
		
		drawgrid(center, screen, hexside, screensize)
		
		pygame.display.flip()
		
	pygame.quit()

def drawgrid(start, screen, hexsize, maxsize):
	toppt = start
	adjsize = hexsize * 1.75
	angle = 0
	coords = (0,0)
	while toppt[0] <= maxsize[0]:
		downpt = toppt
		while 0 <= downpt[1] <= maxsize[1]:
			drawhex(screen, downpt, hexsize, coords)
			hexgrid.append(Hex(downpt, coords))
			
			downpt = [downpt[0], downpt[1] + adjsize]
			coords = (coords[0], coords[1] + 1)
			
		angle = 5 if angle == 6 else 6
		toppt = hexpoint(toppt, adjsize, angle, shift=30)
		
		coords = (coords[0] + 1, angle - 5)
		
def drawhex(screen, center, sidelength, coords = (0,0)):
	if center[0] > 0 and center[1] > 0:
		pts = []
		for i in range(1,7):
			pts.append(hexpoint(center, sidelength, i))
		pygame.draw.polygon(screen, BLACK, pts, 1)
		
		# Write Coordinates on Hex
		text = '({0},{1})'.format(coords[0], coords[1])
		font = pygame.font.SysFont('monospace', 8)
		hextext = font.render(text, True, RED)
		txtsize = font.size(text)
		screen.blit(hextext, (center[0] - (txtsize[0]/2), center[1] - (txtsize[1]/2)))

def hexpoint(center, size, cornerindex, shift = 0):
	anglerad = math.radians((60 * cornerindex) + shift)
	return [center[0] + size * math.cos(anglerad), center[1] + size * math.sin(anglerad)]

class Hex:
	def __init__(self, centerpt, coords):
		self.__center = centerpt
		self.__coords = coords
	
	def __repr__(self):
		return '<Hex ({0}, {1}) ({2}, {3})>'.format(self.__center[0], self.__center[1], self.__coords[0], self.__coords[1])
	
if __name__ == '__main__':
	main()
