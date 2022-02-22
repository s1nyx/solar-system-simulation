from game import *
from math import sqrt, atan2, cos, sin
from globals import *


class Planet:
    DISTANCE_EARTH_SUN = 149.6e6 * 1000  # En mètres
    G = 6.67428e-11
    SCALE = 250 / DISTANCE_EARTH_SUN  # 1DISTANCE_EARTH_SUN = 100 pixels
    TIMESTEP = 86400  # 1 jour en secondes

    def __init__(self, x, y, radius, color, mass, y_velocity, isSun=False):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_velocity = 0
        self.y_velocity = y_velocity

        self.isSun = isSun
        self.distance_to_sun = 0
        self.orbit = []

    def draw(self, window):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []

            for point in self.orbit:
                point_x, point_y = point
                point_x = point_x * self.SCALE + WIDTH / 2
                point_y = point_y * self.SCALE + HEIGHT / 2
                
                updated_points.append((point_x, point_y))

            pygame.draw.lines(window, self.color, False, updated_points, 2)

        pygame.draw.circle(window, self.color, (x, y), self.radius)
        
        if not self.isSun:
            distance_text = COMICSANS_FONT.render(f"{round(self.distance_to_sun / 1000)}km", 1, WHITE_COLOR)
            window.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attractTo(self, other):
        # Calcule de la distance entre les deux planètes
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = sqrt(distance_x**2 + distance_y**2)

        # Si l'autre planète est le soleil on modifie la distance par défaut
        if other.isSun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = atan2(distance_y, distance_x)
        force_x = cos(theta) * force
        force_y = sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_force_x = total_force_y = 0

        for planet in planets:
            if self == planet:
                continue

            force_x, force_y = self.attractTo(planet)
            total_force_x += force_x
            total_force_y += force_y

        self.x_velocity += total_force_x / self.mass * self.TIMESTEP # F = m/a, ici on est sur a = F/m
        self.y_velocity += total_force_y / self.mass * self.TIMESTEP # F = m/a, ici on est sur a = F/m

        self.x += self.x_velocity * self.TIMESTEP
        self.y += self.y_velocity * self.TIMESTEP

        self.orbit.append((self.x, self.y))