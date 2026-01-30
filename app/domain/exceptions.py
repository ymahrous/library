class LibraryError(Exception):
    # Base exception
    pass

class BookNotFoundError(LibraryError):
    pass

class BookUnavailableError(LibraryError):
    pass

class UserNotFoundError(LibraryError):
    pass