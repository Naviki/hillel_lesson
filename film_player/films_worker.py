import os
class film:
    def __init__(self, title, discription, release_year, genre, rating):
        self.title = title
        self.discription = discription
        self.release_year = release_year
        self.genre = genre
        self.rating = rating
        self.storage_address = ''

    def get_title(self):
        return self.title
    def set_title(self, title):
        self.title = title

    def get_discription(self):
        return self.discription

    def set_discription(self, discription):
        self.discription = discription

    def get_release_year(self):
        return self.release_year

    def set_release_year(self, release_year):
        self.release_year = release_year

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_rating(self):
        return self.rating

    def set_rating(self, rating):
        self.rating = rating

    def display_info(self):
        print('Title: ', self.title)
        print('Discription ', self.discription)
        print("Release Year: ", self.release_year)
        print("Genre: ", self.genre)
        print("Rating: ", self.rating)
        print("Storage Address: ", self.storage_address)

    def upload_file(self):
        file_name = self.title + ".txt"
        first_letter = self.title[0]
        storage_directory = os.getcwd() + f'/film_storage/{first_letter}'
        self.storage_address = f'{storage_directory}/{file_name}'
        with open(self.storage_address, 'w') as file:
            file.write(f"Title: {self.title}\n")
            file.write(f"Discription: {self.discription}\n")
            file.write(f"Release Year: {self.release_year}\n")
            file.write(f"Genre: {self.genre}\n")
            file.write(f"Rating: {self.rating}\n")

    def get_film_address(self):
        print(self.storage_address)
        return self.storage_address
"""Тестуємо методи"""
first_film = film("Tarzan", "The movie is about the life of Tarzan. Tarzan was a small orphan who was raised by an ape named Kala since he was a child.", 1999, 'Adventure', 7.3)

first_film.set_title('Tarzan 1') #Задаэмо нову назву фільму

first_film.upload_file() #Створюємо файл

first_film.get_film_address() #Отримуємо шлях до файлу

first_film.display_info() #Отримуємо всю інформацію по фільму


