x = int(input("enter the number of movies: "))
movies = {}

for _ in range(x):
    name = input("movie name:")
    movies[name] = {
        "year": int(input("releaseYear:")),
        "director": input("director:"),
        "pc": float(input("production cost (in crores):")),
        "earning": float(input("collection made (in crores):"))
    }

print("all movie details:")
for name, details in movies.items():
    print(name,": ",details)

print("movies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("movies that made a profit:")
for name, details in movies.items():
    if details["earning"] > details["pc"]:
        print(name)

directorName = input("enter director's name: ")
print("movies directed by",directorName)
for name, details in movies.items():
    if details["director"].lower() == directorName.lower():
        print(name)