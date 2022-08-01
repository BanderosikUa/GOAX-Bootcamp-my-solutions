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

    def test_make_note_and_read(self):
        note = {'film_name': "Hello",
                'note': 'World',
                'rating': '5'}
        expected_result = [self.headers, list(note.values())]
        self.obj.make_note(**note)
        real_result = self.obj.read_notes()

        self.assertEqual(real_result, expected_result)


    @classmethod
    def tearDownClass(cls) -> None:
        cls.obj.delete_csv_file()



if __name__ == '__main__':
    unittest.main()