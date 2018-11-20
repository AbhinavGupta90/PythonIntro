class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country("Poland", 40000000, 452.1),
             Country("Russia", 120000000, 4321.1),
             Country("France", 80000000, 600.5)]

print(countries)
countries.append(Country("Belgium", 3000000, 60.9))
print(countries[1:])