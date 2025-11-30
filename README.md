[README.md](https://github.com/user-attachments/files/23837121/README.md)
# Library Management System

A Python-based library management simulator that models the core operations of a lending library, including item checkout, returns, holds, and fine management.

## Overview

This project implements an object-oriented library system with support for multiple media types (books, albums, and movies), patron management, and automated late fee tracking. It demonstrates inheritance, encapsulation, and class composition in Python.

## Features

- **Multiple item types** with different checkout periods:
  - Books (21 days)
  - Albums (14 days)
  - Movies (7 days)
- **Patron management** with fine tracking
- **Hold system** for requested items
- **Automated late fees** ($0.10/day for overdue items)
- **Item location tracking** (on shelf, on hold, checked out)

## Class Structure

```
LibraryItem (base class)
├── Book
├── Album
└── Movie

Patron
Library
```

## Usage

```python
from Library import Library, Book, Album, Movie, Patron

# Initialize the library
lib = Library()

# Add items
book = Book("b1", "The Great Gatsby", "F. Scott Fitzgerald")
album = Album("a1", "Abbey Road", "The Beatles")
movie = Movie("m1", "Inception", "Christopher Nolan")

lib.add_library_item(book)
lib.add_library_item(album)
lib.add_library_item(movie)

# Add a patron
patron = Patron("p1", "Jane Doe")
lib.add_patron(patron)

# Check out an item
result = lib.check_out_library_item("p1", "b1")
print(result)  # "check out successful"

# Request an item (place a hold)
lib.request_library_item("p1", "m1")

# Return an item
lib.return_library_item("b1")

# Advance time and accumulate fines
for _ in range(30):
    lib.increment_current_date()

# Pay a fine
lib.pay_fine("p1", 0.50)
```

## API Reference

### Library

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `add_library_item()` | LibraryItem | None | Add an item to the library collection |
| `add_patron()` | Patron | None | Register a new patron |
| `check_out_library_item()` | patron_id, item_id | str | Check out an item to a patron |
| `return_library_item()` | item_id | str | Return a checked-out item |
| `request_library_item()` | patron_id, item_id | str | Place a hold on an item |
| `pay_fine()` | patron_id, amount | str | Apply a payment to a patron's fines |
| `increment_current_date()` | None | None | Advance the date by one day |

### Return Messages

- `"check out successful"` / `"return successful"` / `"request successful"` / `"payment successful"`
- `"patron not found"` / `"item not found"`
- `"item already checked out"` / `"item already in library"` / `"item already on hold"`
- `"item on hold by other patron"`

## Requirements

- Python 3.x
- No external dependencies

## Author

Alec Ilstrup ([@ailstrup](https://github.com/ailstrup))

## License

This project is available for educational purposes.
