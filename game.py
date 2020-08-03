import random
import uuid
from datetime import datetime

rows_list = ["8", "7", "6", "5", "4", "3", "2", "1"]
columns_list = ["a", "b", "c", "d", "e", "f", "g", "h"]


def generate_coordinates():
    coordinates = random.choice(columns_list) + random.choice(rows_list)
    return coordinates


class Game:
    id = ""
    guesses = []

    def __init__(self):
        self.guesses.append(Guess())
        self.id = uuid.uuid1()

    @property
    def last_guess(self):
        return self.guesses[-1]

    def try_guess(self, coordinates):
        guess = self.last_guess
        guess.try_coordinates(coordinates)
        return guess.is_guess_valid

    def next_guess(self):
        guess = Guess()
        guesses.append(guess)
        return guess.coordinates_to_guess


class Guess:
    coordinates_to_guess = ''
    coordinates_guessed = ''

    created_timestamp = 0
    guessed_timestamp = 0

    # __init__(self, coordinates):
    #     self.coordinates_to_guess = coordinates
    #     self.created_timestamp = datetime.now().microsecond

    def __init__(self):
        self.coordinates_to_guess = generate_coordinates()
        self.created_timestamp = datetime.now().microsecond

    @property
    def is_guess_valid(self):
        if not self.coordinates_guessed:
            raise Exception("Can't call this method since there was no input")
        return self.coordinates_to_guess == self.coordinates_guessed

    @property
    def delta_timestamps(self):
        if not self.coordinates_guessed:
            raise Exception("Can't call this method since there was no input")
        return self.guessed_timestamp - self.created_timestamp

    def try_coordinates(self, coordinates):
        self.coordinates_to_guess = coordinates
        self.guessed_timestamp = datetime.now().microsecond
