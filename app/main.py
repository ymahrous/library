import uvicorn
from app.api.routes import create_app

if __name__ == "__main__":
    services = bootstrap()
    app = create_app(services)
    uvicorn.run(app, host="127.0.0.1", port=5000)

# library.add_book(Book(1, "1984", "George Orwell", "Dystopia", 15, 2))
# library.add_book(Book(2, "Animal Farm", "George Orwell", "Political", 10, 1))
# print(search.search(author="George Orwell"))
# borrow.borrow(user_id=101, book_id=1)