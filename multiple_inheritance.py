class LandAnimal:
    def walk_behaviour(self):
        print ("I am walking")

class WaterAnimal:
    def swim_behaviour(self):
        print ("I am swimmming")

class Amphibian(LandAnimal, WaterAnimal):
    pass

amphibian = Amphibian()
amphibian.swim_behaviour()
amphibian.walk_behaviour()

