from app import db
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


association_table = db.Table('association_table',
                             db.Column('author_id', db.Integer,
                                       db.ForeignKey('author.id')),
                             db.Column('book_id', db.Integer,
                                       db.ForeignKey('book.id'))
                             )


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), index=True)
    last_name = db.Column(db.String(50), index=True)
    books = db.relationship("Book", secondary=association_table,
                            backref=db.backref("author", lazy='dynamic'))

    def __str__(self):
        return f"<Author {self.first_name} {self.last_name}>"


class State(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.relationship("Book", backref="state", lazy='dynamic')
    avaliable = db.Column(db.Boolean)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    authors = db.relationship("Author", secondary=association_table,
                              backref=db.backref("book", lazy='dynamic'))
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    avaliable = db.Column(db.Integer, db.ForeignKey('state.id'))

    def __str__(self):
        return f"<Post {self.id} {self.title}>"
