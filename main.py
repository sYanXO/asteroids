import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Clock object
    dt = 0  # Delta time variable

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Instantiate the Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit the game to 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

