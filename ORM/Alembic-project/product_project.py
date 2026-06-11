"""
Conversely, declarative mapping makes the process more straightforward by enabling developers to
define the table schema directly within the Python class.
This method automates much of the configuration, as the table and mapper settings are derived
from the class attributes. The declarative style is popular for its simplicity and the clarity it brings to the code.
"""

from typing import List
from sqlalchemy import String, Boolean, ForeignKey, DateTime, create_engine, Text
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker,
)
from datetime import datetime

from sqlalchemy.sql.ddl import CreateTable

from dotenv import load_dotenv
import os

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")


# Define the base class for declarative models
class Base(DeclarativeBase):
    pass


# Define the User model
class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(Text, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(Text, nullable=False)

    # Define a relationship to the Task model
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, username={self.username!r})"


# Define the Task model
class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    test: Mapped[str] = mapped_column(String, nullable=True)

    # Define a relationship to the User model
    user: Mapped[User] = relationship(back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task(task_id={self.task_id!r}, title={self.title!r}, is_completed={self.is_completed!r})"


if __name__ == "__main__":
    # Set up the database connection and session

    # For PostgreSQL
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = "localhost"  # or the IP address of your PostgreSQL server
    port = "5432"  # default PostgreSQL port
    database = "python_web"
    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}"
    )

    # For SQL
    # engine = create_engine("sqlite:///python_web.db")

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Print sql script that sqlalchemy prepared
    print(CreateTable(User.__table__).compile(engine))
    print(CreateTable(Task.__table__).compile(engine))

    # Use SQLAlchemy to add a new User
    user = User(username="Bob", password="bob_password")

    session.add(user)
    session.commit()
    session.close()
