from microlib import NoteObject

notes = NoteObject()
notes.make_note(
    film_name='Hello',
    note='World',
    rating='3'
)
notes.make_note(
    film_name='Something',
    note='Test',
    rating='1'
)
notes.make_note(
    film_name='Spider-Man',
    note='Fild made by Marvel',
    rating='4'
)
notes.print_all()
print(f'Films by minimum rate: {notes.min_rated_films}')
print(f'Films by maximum rate: {notes.max_rated_films}')
print(f'Average films rating: {notes.get_average_rating}')
print()
notes.print_all()
print()
note = notes.read_note(film_name='Spider-Man')
print(note)
notes.delete_note(film_name='Spider-Man')
print()
notes.print_all()

notes.save_to_csv()