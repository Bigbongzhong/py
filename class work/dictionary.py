ppl = {"Naman": "Haridwar", "Badri": "Dehradun", "Kevalya": "Ajmer","Gagan": "Goa", "Suryansh": "Dehradun"}

print("names:", list(ppl.keys()))

print("city_Names:", list(ppl.values()))
print("names-cities:")
for name, city in ppl.items():
    print(name,"-",city)
cc = {}
for city in ppl.values():
    cc[city] = cc.get(city, 0) + 1
print("number of students in each city:")
for city, c in cc.items():
    print(city," - ",c)