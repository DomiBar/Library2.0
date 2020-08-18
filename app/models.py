from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('author_id', Integer,
                                 ForeignKey('author.id')),
                          Column('book_id', Integer, ForeignKey('book.id'))
                          )


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), index=True)
    last_name = db.Column(db.String(50), index=True)
    books = db.relationship("book", secondary=association_table,
                            backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.first_name} {self.last_name}>"


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    authors = db.relationship("author", secondary=association_table,
                              backref="book", lazy="dynamic")
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    cover = db.Column(db.String(200))

    def __str__(self):
        return f"<Post {self.id} {self.title}>"
