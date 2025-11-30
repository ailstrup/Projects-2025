# Author: Alec Ilstrup
# GitHub username: ailstrup
# Date: 11/19/2025
# Description: Library management system simulator with classes for library items, patrons, and library operations

class LibraryItem:
    def __init__(self, library_item_id, title):
        """Initialize a new library item"""
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """Return the unique library item id"""
        return self._library_item_id

    def get_title(self):
        """Return the title of the book"""
        return self._title

    def get_location(self):
        """Return the location of the book: ON_SHELF, ON_HOLD_SHELF, or CHECKED_OUT"""
        return self._location

    def get_checked_out_by(self):
        """Return the name of the person who checked out this book"""
        return self._checked_out_by

    def get_requested_by(self):
        """Return the name of the person who requested this book"""
        return self._requested_by

    def get_date_checked_out(self):
        """Return the date the book was checked out"""
        return self._date_checked_out

    def set_location(self, location):
        """Set the location of the book"""
        self._location = location

    def set_checked_out_by(self, patron):
        """Set the name of the person who checked out this book"""
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        """Update who requested this (patron object or None)"""
        self._requested_by = patron

    def set_date_checked_out(self, date):
        """Update the checked out date of the book"""
        self._date_checked_out = date




class Patron:
    def __init__(self, patron_id, name):
        """Initialize a new patron"""
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """Return the patron id"""
        return self._patron_id

    def get_name(self):
        """Return the name of the patron"""
        return self._name

    def get_checked_out_items(self):
        """Return the checked out items of the patron"""
        return self._checked_out_items

    def get_fine_amount(self):
        """Return the amount that this patron owes in fines"""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Add a library item to the library"""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Remove a library item from the library"""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, amount):
        """amend the fine amount of this patron"""
        self._fine_amount += amount


class Library:
    def __init__(self):
        """initialize a library object"""
        self._holdings = []
        self._members = []
        self._current_date = 0

    def add_library_item(self, library_item):
        """Add a library item to the library"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """Add a patron object to the library"""
        self._members.append(patron)

    def lookup_library_item_from_id(self, library_item_id):
        """Look up a library item by its id"""
        for item in self._holdings:
            if item.get_library_item_id() == library_item_id:
                return item
        return None

    def lookup_patron_from_id(self, patron_id):
        """Look up a patron by its id"""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """Check out a library item by its id"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"

        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if item.get_location() == "ON_HOLD_SHELF":
            if item.get_requested_by() != patron:
                return "item on hold by other patron"

        item.set_checked_out_by(patron)
        item.set_date_checked_out(self._current_date)
        item.set_location("CHECKED_OUT")

        if item.get_requested_by() == patron:
            item.set_requested_by(None)

        patron.add_library_item(item)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """Return a library item"""

        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_location() != "CHECKED_OUT":
            return "item already in library"

        patron = item.get_checked_out_by()
        patron.remove_library_item(item)
        item.set_checked_out_by(None)

        if item.get_requested_by() is not None:
            item.set_location("ON_HOLD_SHELF")
        else:
            item.set_location("ON_SHELF")

        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """request library item by its id"""
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"
        item = self.lookup_library_item_from_id(library_item_id)
        if item is None:
            return "item not found"

        if item.get_requested_by() is not None:
            return "item already on hold"

        item.set_requested_by(patron)

        if item.get_location() == "ON_SHELF":
            item.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self, patron_id, amount):
        patron = self.lookup_patron_from_id(patron_id)
        if patron is None:
            return "patron not found"
        patron.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self):
        self._current_date = (self._current_date + 1)

        for patron in self._members:
            for item in patron.get_checked_out_items():
                days_checked_out = self._current_date - item.get_date_checked_out()

                if days_checked_out > item.get_check_out_length():
                    patron.amend_fine(0.10)


class Book(LibraryItem):
    def __init__(self, library_item_id, title, author):
        """initialize a book item"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        return self._author

    def get_check_out_length(self):
        return 21


class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist):
        """initialize a album item"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        return self._artist

    def get_check_out_length(self):
        return 14


class Movie(LibraryItem):
    def __init__(self, library_item_id, title, director):
        """Initialize a movie item"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        return self._director

    def get_check_out_length(self):
        return 7

