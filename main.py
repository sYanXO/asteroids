import pygame
from constants import *
def main():
      
	# n = 100 
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	clock = pygame.time.Clock() # clcok object
	dt = 0 #delta variable to be used later on

	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
      
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		pygame.display.flip()

		dt = clock.tick(60) / 1000
            

if __name__ == "__main__":
    main() 

