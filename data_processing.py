import csv, os
from pathlib import Path


class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        """Initialize the DataLoader with a base path for data files.
        """
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        """Load a CSV file and return its contents as a list of dictionaries.
        """
        filepath = self.base_path / filename
        data = []

        with filepath.open() as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        tmp = []
        for item in self.table:
            if condition(item):
                tmp.append(item)

        return Table("", tmp)

    # Let's write a function to do aggregation given an aggregation function and an aggregation key
    def aggregate(self,aggregation_function, aggregation_key):
        tmp = []
        for i in self.table:
            try:
                tmp.append(float(i[aggregation_key]))
            except ValueError:
                tmp.append(i[aggregation_key])

        return Table("", aggregation_function(tmp))

    def join(self, joining, join_key):
        new = self.table.copy()
        for i in new:
            for j in joining.table:
                if i[join_key] == j[join_key]:
                    i.update(j)

        return Table("", new)

    def __str__(self):
        return self.table_name + ':' + str(self.table)


class DB:
    def __init__(self):
        self.__tables = []

    def insert(self, table: Table):
        self.__tables.append(table)

    def search(self, table_name):
        for i in self.__tables:
            if i.table_name == table_name:
                return i

        return None


loader = DataLoader()
cities = loader.load_csv('Cities.csv')
table1 = Table('cities', cities)
countries = loader.load_csv('Countries.csv')
table2 = Table('countries', countries)

my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)

my_table1 = my_DB.search('cities')
print("List all cities in Italy:")
my_table1_filtered = my_table1.filter(lambda x: x['country'] == 'Italy')
print(my_table1_filtered)
print()

print("Average temperature for all cities in Italy:")
print(my_table1_filtered.aggregate(lambda x: sum(x) / len(x), 'temperature'))
print()

my_table2 = my_DB.search('countries')
print("List all non-EU countries:")
my_table2_filtered = my_table2.filter(lambda x: x['EU'] == 'no')
print(my_table2_filtered)
print()

print("Number of countries that have coastline:")
print(my_table2.filter(lambda x: x['coastline'] == 'yes').aggregate(lambda x: len(x), 'coastline'))
print()

my_table3 = my_table1.join(my_table2, 'country')
print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()

print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'no').filter(lambda x: float(x['temperature']) < 5.0)
print(my_table3_filtered.table)
print()

print("The min and max temperatures for cities in EU countries that do not have coastlines")
my_table3_filtered = my_table3.filter(lambda x: x['EU'] == 'yes').filter(lambda x: x['coastline'] == 'no')
print("Min temp:", my_table3_filtered.aggregate(lambda x: min(x), 'temperature'))
print("Max temp:", my_table3_filtered.aggregate(lambda x: max(x), 'temperature'))
print()