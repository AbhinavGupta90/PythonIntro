from operator import attrgetter

class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country("Poland", 40000001, 452.1),
             Country("Russia", 120000000, 4321.1),
             Country("France", 80000005, 600.5)]

print(countries)
countries.append(Country("Belgium", 3000000, 60.9))
print(countries[1:])

countries.sort(key=attrgetter('population'), reverse=True)
country_with_max_population = max(countries, key=attrgetter('population'))
country_with_max_area = max(countries, key=attrgetter('area'))
country_with_min_population = min(countries, key=attrgetter('population'))
print(country_with_max_population)
print(country_with_min_population)
print(country_with_max_area)
print(countries)

##list comprehension

countries = countries + [Country("Bosnia", 3500437, 32.5),
                         Country("Spain", 50000124, 132.4),
                         Country("Chechia", 3990119, 83.1),
                         Country("Slovakia", 3000211, 50.2)]

print(countries)
countries_with_population_bigger_than_4_million = []

for country in countries:
    if country.population >= 4000000:
        countries_with_population_bigger_than_4_million.append(country)

print(countries_with_population_bigger_than_4_million)

countries_names_in_uppercase = [country.name.upper() for country in countries]
print(countries_names_in_uppercase)

countries_with_area_less_than_100 = [country for country in countries if country.area <= 100]
print(countries_with_area_less_than_100)

countries_with_even_population = [country for country in countries if country.population%2 == 0]
print(countries_with_even_population)