from sqlalchemy import (create_engine, func, ForeignKey,
    Index, Table, Column, Integer, String)
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, session

engine = create_engine('sqlite:///restaurants.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    price = Column(Integer())

    reviews = relationship('Review', back_populates='restaurant')
    customers = association_proxy('reviews', 'customer',
        creator=lambda cs: Review(customer=cs))

    def __repr__(self):
        return f"Restaurant {self.id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String())

    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant',
        creator=lambda rs: Review(restaurant=rs))

    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name}, " \
            + f"{self.last_name}"
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'rating={self.star_rating}, ' + \
            f'restaurant_id={self.restaurant_id})'