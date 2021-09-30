from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Members(db.Model):

    name = db.Column(db.String(255))
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Books(db.Model):

    id = db.Column(db.String(20), primary_key=True)
    book_name = db.Column(db.String(255))
    publisher = db.Column(db.String(255))
    author = db.Column(db.String(255))
    publication_date = db.Column(db.String(255))
    pages = db.Column(db.String(4))
    isbn = db.Column(db.String(255))
    description = db.Column(db.String(255))
    link = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    image_path = db.Column(db.String(256))

    def __init__(self, id, book_name, publisher, author, publication_date, pages, isbn, description, link, rating, stock, image_path):
        self.id = id
        self.book_name = book_name
        self.publisher = publisher
        self.author = author
        self.publication_date = publication_date
        self.pages = pages
        self.isbn = isbn
        self.description = description
        self.link = link
        self.rating = rating
        self.stock = stock
        self.image_path = image_path
