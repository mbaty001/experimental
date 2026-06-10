from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Product class mapped to the 'products' table
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)

# Set up the database connection and session
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in the database which are defined by Base's subclasses such as Product
Base.metadata.create_all(engine)

# Use SQLAlchemy to add a new product
product = Product(name='Laptop', price=999.99)
session.add(product)
session.commit()

