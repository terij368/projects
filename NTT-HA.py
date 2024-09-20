import json

class Film:
    def __init__(self, title, year, director, actors, rating):
        self.title = title
        self.year = year
        self.director = director
        self.actors = actors
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.director} - {self.actors} - {self.rating}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "actors": self.actors,
            "rating": self.rating
        }
    
class Database:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.load()
    
    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = []
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f)
    
    def add_film(self, film):
        self.data.append(film.to_dict())
        self.save()
    
    def get_films(self):
        films = []
        for film in self.data:
            films.append(Film(film["title"], film["year"], film["director"], film["actors"], film["rating"]))
        return films
    
    def delete_film(self, title):
        updated_data = []
        for film in self.data:
            if film["title"] != title:
                updated_data.append(film)
        self.data = updated_data
        self.save()
    
    def update_film(self, title, new_film):
        for film in self.data:
            if film["title"] == title:
                film.update(new_film.to_dict())
                self.save()
                break
            
def main():
    db = Database("films.json")
    while True:
        print("1. List films")
        print("2. Add film")
        print("3. Update film")
        print("4. Delete film")
        print("5. Exit")
        print("6. Earliest year film")
        print("7. Latest year film")
        choice = input("Choose option: ")
        if choice == "1":
            films = db.get_films()
            for film in films:
                print(film)
        elif choice == "2":
            title = input("Title: ")
            year = input("Year: ")
            director = input("Director: ")
            actors = input("Actors: ")
            rating = input("Rating: ")
            film = Film(title, year, director, actors, rating)
            db.add_film(film)
        elif choice == "3":
            title = input("Title: ")
            year = input("Year: ")
            director = input("Director: ")
            actors = input("Actors: ")
            rating = input("Rating: ")
            film = Film(title, year, director, actors, rating)
            db.update_film(title, film)
        elif choice == "4":
            title = input("Title: ")
            db.delete_film(title)
        elif choice == "5":
            break
        elif choice == "6":
            films = db.get_films()
            if films:
                def get_year(film):
                    return film.year
                earliest = min(films, key=get_year)
                print(earliest)
        elif choice == "7":
            films = db.get_films()
            if films:
                def get_year(film):
                    return film.year
                latest = max(films, key=get_year)
                print(latest)
        else:
            print("Invalid option")

main()

# Unit test
import unittest

class TestFilmDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database("test_films.json")
        
    def test_add_film(self):
        film = Film("Test", 2021, "Test Director", "Test Actor", 10)
        self.db.add_film(film)
        films = self.db.get_films()
        self.assertEqual(len(films), 1)
        self.assertEqual(films[0].title, "Test")
        self.assertEqual(films[0].year, 2021)
        self.assertEqual(films[0].director, "Test Director")
        self.assertEqual(films[0].actors, "Test Actor")
        self.assertEqual(films[0].rating, 10)
        
    def test_delete_film(self):
        film = Film("Test", 2021, "Test Director", "Test Actor", 10)
        self.db.add_film(film)
        self.db.delete_film("Test")
        films = self.db.get_films()
        self.assertEqual(len(films), 0)
        
    def test_update_film(self):
        film = Film("Test", 2021, "Test Director", "Test Actor", 10)
        self.db.add_film(film)
        new_film = Film("Test2", 2022, "Test Director 2", "Test Actor 2", 9)
        self.db.update_film("Test", new_film)
        films = self.db.get_films()
        self.assertEqual(len(films), 1)
        self.assertEqual(films[0].title, "Test2")
        self.assertEqual(films[0].year, 2022)
        self.assertEqual(films[0].director, "Test Director 2")
        self.assertEqual(films[0].actors, "Test Actor 2")
        self.assertEqual(films[0].rating, 9)

unittest.main()