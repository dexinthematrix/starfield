import pygame
import random
import math
from pygame.sprite import Sprite
import sys


class Star(Sprite):
    """A class to define the geometry of the star"""

    def __init__(self):
        """Create a star at screen centre"""
        super(Star, self).__init__()
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.red, self.green, self.blue = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.red_up = True
        self.green_up = True
        self.blue_up = False
        self.count = 1
        self.clock = False

        #  Define the initial position of the star
        self.a, self.b = self.screen_width / 2, self.screen_height / 2
        # Define the initial size of the star
        self.d = 0.1
        # Define the initial direction of the star
        self.direction = random.random() * 2 * math.pi
        # Define the initial offset from the start position
        self.dist = 0
        # Define the star points - call function
        self.star_points()

    def swirl_direction(self):
        """Determines the direction of the swirl"""
        # This parameter sets the number of cycles between direction changes
        self.swirl = 150
        # This bit checks if the cycle count is divisible by the interval and reverses the direction if so.
        if self.count % self.swirl == 0 and self.clock:
            self.clock = False
        elif self.count % self.swirl == 0 and not self.clock:
            self.clock = True

        self.count += 1

    def update_star(self):
        """Move the star"""
        self.d += 0.002
        self.dist += 0.005
        # Runs the routine to determine the direction of the swirl
        self.swirl_direction()
        # This bit makes the swirl in the appropriate direction
        if self.clock:
            self.direction -= 0.005
        else:
            self.direction += 0.005
        # This bit adds the distance and resolves it to x and y directions (a and b)
        self.a += self.dist * math.sin(self.direction)
        self.b += self.dist * math.cos(self.direction)
        self.star_points()

    def star_points(self):
        self.points = (
            (self.a + 6 * self.d, self.b), (self.a + 8 * self.d, self.b + 3 * self.d),
            (self.a + 12 * self.d, self.b + 3 * self.d), (self.a + 10 * self.d, self.b + 6 * self.d),
            (self.a + 12 * self.d, self.b + 9 * self.d), (self.a + 8 * self.d, self.b + 8 * self.d),
            (self.a + 6 * self.d, self.b + 12 * self.d), (self.a + 4 * self.d, self.b + 8 * self.d),
            (self.a, self.b + 9 * self.d), (self.a + 2 * self.d, self.b + 6 * self.d), (self.a, self.b + 3 * self.d),
            (self.a + 4 * self.d, self.b + 3 * self.d))

    def draw_star(self):
        """Draw the start to the screen"""
        self.get_color()
        pygame.draw.polygon(self.screen, (self.red, self.green, self.blue),
                            self.points)

    def get_color(self):
        """Check whether colour value to go up or down and then amend"""
        # Red
        if self.red_up and self.red == 255:
            self.red_up = False
        elif not self.red_up and self.red == 0:
            self.red_up = True
        if self.red < 255 and self.red_up:
            self.red += 1
        else:
            self.red -= 1
        # Green
        if self.green_up and self.green == 255:
            self.green_up = False
        elif not self.green_up and self.green == 0:
            self.green_up = True
        if self.green < 255 and self.green_up:
            self.green += 1
        else:
            self.green -= 1
        # Blue
        if self.blue_up and self.blue == 255:
            self.blue_up = False
        elif not self.blue_up and self.blue == 0:
            self.blue_up = True
        if self.blue < 255 and self.blue_up:
            self.blue += 1
        else:
            self.blue -= 1


def run_game():
    pygame.init()
    bg_color = (10, 10, 10)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width = screen.get_rect().width
    screen_height = screen.get_rect().height
    pygame.display.set_caption("Starfield")
    stars = pygame.sprite.Group()

    while True:
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eve.type == pygame.KEYDOWN and eve.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        screen.fill(bg_color)

        star = Star()
        stars.add(star)
        for star in stars.sprites():
            star.update_star()
            star.draw_star()
            if star.a > screen_width or star.a < 0 or star.b > screen_height or star.b < 0:
                stars.remove(star)

        pygame.display.flip()


run_game()
