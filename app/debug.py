from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Review, Customer

# Create an SQLite database (you can replace 'sqlite:///your_database.db' with your preferred database URL).
engine = create_engine('sqlite:///restaurants.db')

# Create the tables in the database.
Base.metadata.create_all(engine)

# Create a session to interact with the database.
Session = sessionmaker(bind=engine)
session = Session()

rest1 = session.query(Restaurant).first()
cust1 = session.query(Customer).first()
rev1 = session.query(Review).first()

print("Review customer: ")
print(rev1.rev_customer())
print("Review restaurant: ")
print(rev1.rev_restaurant())

print(" ")
print("Restaurant Reviews: ")
print(rest1.rest_reviews())
print("Restaurant customers: ")
print(rest1.rest_customers())

print(" ")
print("Customer reviews: ")
print(cust1.cust_reviews())
print("Customer restaurants: ")
print(cust1.cust_restaurants())

print(" ")
print("Customer full_name: ")
print(cust1.full_name())
print("Customer favorite_restaurant: ")
print(cust1.favorite_restaurant())

print(" ")
print("Review full_review: ")
print(rev1.full_review())

