#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Restaurant, Customer, Review

engine = create_engine('sqlite:///restaurants.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

if __name__ == '__main__':
    
    print("Clearing DB")
    session.query(Restaurant).delete()
    session.query(Customer).delete()
    session.query(Review).delete()

    print("Seeding Restaurants, Customers and Reviews...")
    rests = []
    for i in range(10):
        new_restaurant = Restaurant(name=fake.unique.company(), price=random.randint(1000, 15000))
        session.add(new_restaurant)
        session.commit()
        rests.append(new_restaurant)
    print("Seeded Restaurants")


    custs = []
    for i in range(15):
        new_customer = Customer(first_name=fake.unique.first_name(), last_name=fake.unique.last_name())
        session.add(new_customer)
        session.commit()
        custs.append(new_customer)
    print("Seeded Customers")

    for rest in rests:
        new_review = [(Review(star_rating = random.randint(1,10), customer_id =(random.choice(custs)).id, restaurant_id = rest.id)) for i in range(3)]
        session.add_all(new_review)
        session.commit()
    print("Seeded Reviews")

session.close()