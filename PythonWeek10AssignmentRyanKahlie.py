class SolarObject:
    def __init__(self, farthest_distance, orbit_days):
        self.farthest_distance = farthest_distance
        self.spin_type = "unknown"
        self.orbit_days = orbit_days
#calculating the possible population based on distance from the sun
    def colonization(self):
        possible_population = 6000000000 / self.farthest_distance
        #rounding to 2 decimals
        return round(possible_population, 2)

    #will be used in the sub-classes with their respective value
    def spin(self):
        pass

#class for planets that defines the spin type as slightly elliptical
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

#looked up the AU for distance from the sun, and the orbit of the sun
#in days to pass through the classes functions
earth = Planet(1.02, 365.25)
mars = Planet(1.67, 687)
halley = Comet(35.14, 27500)
hale_bopp = Comet(370.8, 863000)

#used to speed up iteration with a list vs writing out a print statement for each
#one individually
space_rocks = [
    ("Earth", earth),
    ("Mars", mars),
    ("Halley Comet", halley),
    ("Hale-Bopp", hale_bopp),
]

#uses space rocks function to print the same series with iteration
#for the name, object
for name, obj in space_rocks:
    print(f"Space Rocks: {name}")
    print(f"   Farthest Distance: {obj.farthest_distance} AU")
    print(f"   Rotates: {obj.spin()}")
    print(f"   Orbit in years: {round(obj.orbit_days / 365.25, 2)} Years")
    print(f"   Potential Population: {obj.colonization()} Lives")

