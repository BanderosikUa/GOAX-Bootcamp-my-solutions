import csv
import pandas as pd

from pathlib import Path


class NoteObject:
    def __init__(self, csv_file: str = None):
        self.BASE_DIR = Path('.')
        if csv_file:
            location = Path(csv_file)
        else:
            location = self.BASE_DIR.joinpath('notes.csv')
        if not location.exists():
            location.touch()

        self.make_note(
            film_name='film_name',
            note='note',
            rating='rating'
        )

    @staticmethod
    def read_csv(func):
        def wrapper(self, *args, **kwargs):
            csv_file = open(
                self.BASE_DIR / 'notes.csv',
                'r',
                encoding='UTF-8')
            result = func(self, csv_file, *args, **kwargs)
            csv_file.close()
            return result

        return wrapper

    @staticmethod
    def write_csv(func):
        def wrapper(self, *args, **kwargs):
            csv_file = open(
                self.BASE_DIR / 'notes.csv',
                'a',
                encoding='UTF-8')
            result = func(self, csv_file, *args, **kwargs)
            csv_file.close()
            return result

        return wrapper

    @write_csv
    def make_note(self, csv_file,
                  *,
                  film_name: str,
                  note: str,
                  rating: int | str):
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow([film_name, note, rating])

    @read_csv
    def read_notes(self, csv_file) -> list:
        csv_reader = csv.reader(csv_file)
        return list(csv_reader)

    @write_csv
    def delete_row(self, film_name):



    def delete_csv_file(self):
        self.BASE_DIR.joinpath('notes.csv').unlink()


