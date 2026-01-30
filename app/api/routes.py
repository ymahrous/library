class Routes:
    def __init__(self, library_service, borrowing_service, search_service):
        self.library = library_service
        self.borrowing = borrowing_service
        self.search = search_service