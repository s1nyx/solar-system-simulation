from core.globals import *
from managers.planet_manager import PlanetManager

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")


def main():
    should_run = True
    clock = pygame.time.Clock()

    solar_system = PlanetManager()
    solar_system.populate_planets()

    while should_run:
        clock.tick(60)
        WINDOW.fill(BLACK_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                should_run = False

        for planet in solar_system.planets:
            planet.update_position(solar_system.planets)
            planet.draw(WINDOW)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()