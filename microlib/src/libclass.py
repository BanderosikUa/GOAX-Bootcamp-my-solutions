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
        self.headers = ['film_name', 'note', 'rating']
        if location.exists():
            self.df = pd.read_csv(location)
        else:
            self.df = pd.DataFrame(columns=self.headers)

    def make_note(self,
                  *,
                  film_name: str,
                  note: str,
                  rating: int | str):
        if int(rating) not in range(1, 6):
            raise ValueError('Rating must be in range from 1 to 5')
        data = pd.DataFrame([[film_name, note, int(rating)]],
                            columns=self.headers)
        if film_name in self.df.film_name.values:
            print('This film already exists')
        else:
            self.df = pd.concat([self.df, data],
                                 ignore_index=True)

    def print_all(self) -> list:
        print(self.df.to_string())

    def read_note(self, *, film_name: str) -> str:
        row = self.df.loc[self.df['film_name'] == film_name]
        if row.empty:
            response = 'This film not in file'
        else:
            response = row.values.tolist()[0][1]
        return response

    def delete_note(self, *, film_name: str):
        self.df = self.df[self.df.film_name != film_name]
        print(f'Deleted "{film_name}"')

    @property
    def min_rated_films(self) -> list:
        min_value = self.df.rating.min()
        rows = self.df[self.df.rating == min_value]
        return rows.values.tolist()

    @property
    def max_rated_films(self) -> list:
        max_value = self.df.rating.max()
        rows = self.df[self.df.rating == max_value]
        return rows.values.tolist()

    @property
    def get_average_rating(self) -> int:
        ratings = self.df['rating']
        return pd.to_numeric(ratings).mean()

    def save_to_csv(self) -> None:
        self.df.to_csv('result.csv', index=False)
