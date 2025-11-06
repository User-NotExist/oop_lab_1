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

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    tmp = []
    for item in dict_list:
        if condition(item):
            tmp.append(item)

    return tmp

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    tmp = []
    for i in dict_list:
        try:
            tmp.append(float(i[aggregation_key]))
        except ValueError:
            tmp.append(i[aggregation_key])

    return aggregation_function(tmp)



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
filtered_list = filter(lambda x:x['country'] == 'Germany', cities)
print(filtered_list)
print()

# Print all cities in Spain with a temperature above 12°C
print("Cities in sPain where temperature is above 12: ")
spain_cities = filter(lambda x : x["country"] == "Spain" and float(x["temperature"]) > 12, cities)
print(spain_cities)
print()

# Count the number of unique countries
print("Country")
print(len(set(city['country'] for city in cities)))
print()

# Print the average temperature for all the cities in Germany
print("Avg temp in germany")
german_cities = filter(lambda x : x['country'] == 'Germany', cities)
print(sum(aggregate('temperature', lambda x : x, german_cities)) / len(german_cities))
print()

# Print the max temperature for all the cities in Italy
print("Max temp in Italy: ")
print(aggregate("temperature", max, filter(lambda x : x['country'] == 'Italy', cities)))