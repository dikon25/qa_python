from main import BooksCollector

class TestBooksCollector:

     def test_add_new_book_add_two_books(self,collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

     def test_set_book_genre_for_add_books(self,collector):
        name='Гордость и предубеждение и зомби'
        genre='Ужасы'
        test={name:genre}
        collector.add_new_book(name)
        collector.set_book_genre(name,genre)
        assert collector.get_books_genre()==test
     def test_get_books_with_specific_genre(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.get_books_with_specific_genre('Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы')==['Гордость и предубеждение и зомби']
     def test_add_new_book_without_genre(self,collector):
        name = 'Что делать, если ваш кот хочет вас убить'
        collector.add_new_book(name)
        assert collector.get_books_genre()!= None
     def test_get_books_for_children_without_age_rating(self,collector):
        name_child='Что делать, если ваш котхо чет вас убить'
        name_adult='Гордость и предубеждение и зомби'
        genre_child='Комедия'
        genre_adult='Ужасы'
        collector.add_new_book(name_adult)
        collector.set_book_genre(name_adult, genre_adult)
        collector.add_new_book(name_child)
        collector.set_book_genre(name_child, genre_child)
        assert name_adult not in collector.get_books_for_children()
     def test_add_book_in_favorites(self,collector):
        book='Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert book in collector.get_list_of_favorites_books()
     def test_delete_book_from_favorites(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books())==0
     def test_get_list_of_favorites_books(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books()!=None

     def test_add_same_book_in_favorites(self,collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books())==1