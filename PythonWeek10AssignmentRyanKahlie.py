class SolarObject:
    def __init__(self, farthest_distance, orbit_days):
        self.farthest_distance = farthest_distance
        self.spin_type = "unknown"
        self.orbit_days = orbit_days

    def colonization(self):
        possible_population = 6000000000 / self.farthest_distance
        return round(possible_population, 2)

    def spin(self):
        pass

class Planet(SolarObject):
    def __init__(self, farthest_distance, orbit_days):
        super().__init__(farthest_distance, orbit_days)
        self.spin_type = "slightly elliptical"

    def spin(self):
        return self.spin_type

class Comet(SolarObject):
    def __init__(self, farthest_distance, orbit_days):
        super().__init__(farthest_distance, orbit_days)
        self.spin_type = "like crazy"

    def spin(self):
        return self.spin_type


earth = Planet(1.02, 365.25)
mars = Planet(1.67, 687)
halley = Comet(35.14, 27500)
hale_bopp = Comet(370.8, 863000)


space_rocks = [
    ("Earth", earth),
    ("Mars", mars),
    ("Halley Comet", halley),
    ("Hale-Bopp", hale_bopp),
]


for name, obj in space_rocks:
    print(f"Space Rocks: {name}")
    print(f"   Farthest Distance: {obj.farthest_distance} AU")
    print(f"   Rotates: {obj.spin()}")
    print(f"   Orbit in years: {round(obj.orbit_days / 365.25, 2)} Years")
    print(f"   Potential Population: {obj.colonization()} Lives")

