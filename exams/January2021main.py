from January2021 import City

city1 = City(20,20)


city1.create_streets()
city1.create_snowplows()

city1.snow(100)

print(city1.streets_to_clean())

city1.clean_street()

print("Streets not cleaned:")
print(city1.streets_to_clean())
