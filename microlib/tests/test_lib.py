import unittest
import csv

from ..src import libclass


class TestNoteObject(unittest.TestCase):
    # def test_create_object(self):
    #     note = libclass.NoteObject()
    @classmethod
    def setUpClass(cls) -> None:
        cls.obj = libclass.NoteObject()
        cls.headers = ['film_name', 'note', 'rating']

    def test_make_note(self):
        note = {'film_name': "Hello",
                'note': 'World',
                'rating': 5}
        self.obj.make_note(**note)
        result = self.obj.df[self.obj.df.film_name == note['film_name']].values.tolist()
        self.assertEqual(result, [list(note.values())])

    def test_make_note_duplicate(self):
        """Check note creating if film already in file"""
        note = {'film_name': "Hello",
                'note': 'World',
                'rating': 5}
        self.obj.make_note(**note)
        result = len(self.obj.df[self.obj.df.film_name == note.get('film_name')])
        self.assertEqual(result, 1)

    def test_rating_out_range(self):
        note = {'film_name': "Hello",
                'note': 'World',
                'rating': 6}
        try:
            self.obj.make_note(**note)
        except ValueError as error:
            assert True

    def test_read_note(self):
        real_result = self.obj.read_note(film_name='Hello')
        expected_result = 'World'

        self.assertEqual(real_result, expected_result)

    def test_delete_note(self):
        self.obj.delete_note(film_name='Hello')

        real_result = self.obj.read_note(film_name='Hello')

        self.assertEqual(real_result, 'This film not in file')

    def test_min_rating(self):
        note = {'film_name': "Hello1",
                'note': 'World',
                'rating': 1}
        self.obj.make_note(**note)
        note = {'film_name': "Hello2",
                'note': 'World',
                'rating': 2}
        self.obj.make_note(**note)
        note = {'film_name': "Hello3",
                'note': 'World',
                'rating': 1}
        self.obj.make_note(**note)

        expected_response = [['Hello1', 'World', 1], ['Hello3', 'World', 1]]
        real_response = self.obj.min_rated_films

        self.assertEqual(expected_response, real_response)

    def test_max_rating(self):
        note = {'film_name': "Hello4",
                'note': 'World',
                'rating': 3}
        self.obj.make_note(**note)
        note = {'film_name': "Hello5",
                'note': 'World',
                'rating': 4}
        self.obj.make_note(**note)
        note = {'film_name': "Hello6",
                'note': 'World',
                'rating': 5}
        self.obj.make_note(**note)

        expected_response = [['Hello', 'World', 5],
                             ['Hello6', 'World', 5]]
        real_response = self.obj.max_rated_films

    def test_average_rating(self):
        note = {'film_name': "Hello4",
                'note': 'World',
                'rating': 3}
        self.obj.make_note(**note)
        note = {'film_name': "Hello5",
                'note': 'World',
                'rating': 5}
        self.obj.make_note(**note)
        note = {'film_name': "Hello6",
                'note': 'World',
                'rating': 4}
        self.obj.make_note(**note)

        expected_response = 4.0
        real_response = self.obj.get_average_rating

        self.assertEqual(expected_response, real_response)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.obj.df.drop(cls.obj.df.index, inplace=True)



if __name__ == '__main__':
    unittest.main()