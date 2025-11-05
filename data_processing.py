import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("Cities in germany: ")
german_cities = set()
for city in cities:
    if city['country'] != 'Germany':
        continue

    german_cities.add(city["city"])

print(german_cities)
print()

# Print all cities in Spain with a temperature above 12°C
print("Cities in sPain where temperature is above 12: ")
spain_cities = set()
for city in cities:
    if city['country'] != 'Spain' or float(city['temperature']) < 12:
        continue

    spain_cities.add(city["city"])

print(spain_cities)
print()

# Count the number of unique countries
print("Country")
countries = set(city['country'] for city in cities)
print(len(countries))
print()

# Print the average temperature for all the cities in Germany
print("Avg temp in germany")
temp = []
for city in cities:
    if city['country'] != 'Germany':
        continue

    temp.append(float(city['temperature']))
print(sum(temp) / len(temp))
print()

# Print the max temperature for all the cities in Italy
print("Max temp in Italy: ")

highest = None

for city in cities:
    if city['country'] != 'Italy':
        continue

    if highest is None:
        highest = city
        continue

    if float(highest['temperature']) < float(city['temperature']):
        highest = city

print(highest['temperature'])