from game import *
from entities.planet import Planet
from globals import *


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Solar System Simulation")

planets = []


def create_planet(planet):
    planets.append(planet)


def main():
    shouldRun = True
    clock = pygame.time.Clock()

    create_planet(Planet(0, 0, 30, YELLOW_COLOR, 1.98892 * 10**30, 0, True))  # Sun
    create_planet(Planet(-1 * Planet.DISTANCE_EARTH_SUN, 0, 16, BLUE_COLOR, 5.9742 * 10**24, 29.783 * 1000))  # Earth
    create_planet(Planet(-1.524 * Planet.DISTANCE_EARTH_SUN, 0, 12, RED_COLOR, 6.39 * 10**23, 24.077 * 1000))  # Mars
    create_planet(Planet(0.387 * Planet.DISTANCE_EARTH_SUN, 0, 8, DARK_GREY_COLOR, 3.3 * 10**23, -47.4 * 1000))  # Mercure
    create_planet(Planet(0.723 * Planet.DISTANCE_EARTH_SUN, 0, 14, WHITE_COLOR, 4.8685 * 10**24, -35.02 * 1000))  # Venus

    while shouldRun:
        clock.tick(60)
        WINDOW.fill(BLACK_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shouldRun = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()

main()