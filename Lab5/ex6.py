import datetime


class LibraryItem:
    def __init__(self, title, lib_number):
        self.title = title
        self.lib_number = lib_number
        self.date_due = None

    def check_out(self):
        self.date_due = datetime.datetime.now() + datetime.timedelta(days=14)
        print(f'Checking out item {self.lib_number}, next due date is {self.date_due}')

    def return_item(self):
        if self.date_due < datetime.datetime.now():
            print(f'Item {self.lib_number} is overdue.')


class Book(LibraryItem):
    def __init__(self, title, lib_number, author, year, num_pages, genre):
        super().__init__(title, lib_number)
        self.author = author
        self.num_pages = num_pages
        self.genre = genre
        self.year = year

    def __str__(self):
        return (f'Book {self.title} by {self.author}, written in {self.year}. '
                f'\n Genre: {self.genre} '
                f'\n Number of pages: {self.num_pages} ')


class DVD(LibraryItem):
    def __init__(self, title, lib_number, year, run_time):
        super().__init__(title, lib_number)
        self.run_time = run_time
        self.year = year

    def __str__(self):
        return (f'DVD {self.title} from {self.year}. '
                f'\n Run time: {self.run_time} minutes ')


class Magazine(LibraryItem):
    def __init__(self, title, lib_number, issue, publisher, year):
        super().__init__(title, lib_number)
        self.issue = issue
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return (f'Magazine {self.title} from {self.year}. '
                f'\n Issue: {self.issue} '
                f'\n Publisher: {self.publisher} ')


def main():
    book = Book('The Lord of the Rings', '759', 'J. R. R. Tolkien', '1954', '1178', 'Fantasy')
    print(book)
    book.check_out()
    book.return_item()
    print()

    dvd = DVD('The Lord of the Rings', '1882', '2001', '178')
    print(dvd)
    dvd.check_out()
    dvd.return_item()
    print()

    magazine = Magazine('Vogue', '1985', '1', 'Conde Nast', '2010')
    print(magazine)
    magazine.check_out()
    magazine.return_item()
    print()


if __name__ == '__main__':
    main()

