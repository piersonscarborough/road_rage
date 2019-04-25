import pygame

# Create Vehicle Class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

# Create Player Class that inherits from Car Class

class Player(Vehicle):
    pass


def main():
    
    # Initialize game window
    width = 1200
    height = 600
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

    # Game initialization
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Draw background
        screen.fill(blue_color)
        #screen.blit(background_image, [0, 0])

        # Draw player, enemy, and other vehicles

        # Game display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()