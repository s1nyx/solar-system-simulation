from entities.planet import Planet
from core.globals import *


class PlanetManager:
    def __init__(self):
        self.planets = []

    def __add_planet(self, planet):
        self.planets.append(planet)

    def populate_planets(self):
        """
        Populate the list of planets with basics one from our galaxy
        """
        self.__add_planet(Planet("Soleil", 0, 0, 30, YELLOW_COLOR, 1.98892 * 10 ** 30, 0, True))  # Sun
        self.__add_planet(Planet("Mercure", 0.387 * Planet.DISTANCE_EARTH_SUN, 0, 8, DARK_GREY_COLOR, 3.3 * 10 ** 23, -47.4 * 1000))  # Mercure
        self.__add_planet(Planet("Vénus", 0.723 * Planet.DISTANCE_EARTH_SUN, 0, 14, WHITE_COLOR, 4.8685 * 10 ** 24, -35.02 * 1000))  # Venus
        self.__add_planet(Planet("Terre", -1 * Planet.DISTANCE_EARTH_SUN, 0, 16, BLUE_COLOR, 5.9742 * 10 ** 24, 29.783 * 1000))  # Earth
        self.__add_planet(Planet("Mars", -1.524 * Planet.DISTANCE_EARTH_SUN, 0, 12, RED_COLOR, 6.39 * 10 ** 23, 24.077 * 1000))  # Mars
        #self.__add_planet(Planet("Jupyter", -2.227 * Planet.DISTANCE_EARTH_SUN, 0, 8, RED_COLOR, 6.42 * 10 ** 23, 13.11 * 1000))  # Mars
