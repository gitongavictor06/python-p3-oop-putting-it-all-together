class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self._current_page = 1  # Starting at page 1 by default
        self._bookmarks = set()  # Using a set to avoid duplicate bookmarks

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            raise TypeError("page_count must be an integer")
        if value <= 0:
            raise ValueError("page_count must be a positive integer")
        self._page_count = value

    @property
    def current_page(self):
        return self._current_page

    def turn_page(self):
        if self._current_page < self.page_count:
            self._current_page += 1
        else:
            print("You've reached the end of the book!")
        return self

    def add_bookmark(self, page_number):
        if not isinstance(page_number, int):
            raise TypeError("Bookmark page must be an integer")
        if page_number < 1 or page_number > self.page_count:
            raise ValueError("Bookmark page must be within the book's pages")
        self._bookmarks.add(page_number)

    def remove_bookmark(self, page_number):
        if page_number in self._bookmarks:
            self._bookmarks.remove(page_number)

    def get_bookmarks(self):
        return sorted(self._bookmarks)  # Return sorted list of bookmarks

    def __str__(self):
        return f"Book: {self.title} ({self.page_count} pages)"

    def __repr__(self):
        return f"Book(title='{self.title}', page_count={self.page_count})"