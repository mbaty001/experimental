from typing import List
from sqlalchemy import String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from datetime import datetime

# Define the base class for declarative models
class Base(DeclarativeBase):
    pass

# Define the User model
class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)

    # Define a relationship to the Task model
    tasks: Mapped[List["Task"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id!r}, username={self.username!r})"

# Define the Task model
class Task(Base):
    __tablename__ = 'tasks'

    task_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    description: Mapped[str|None]

    # Define a relationship to the User model
    user: Mapped[User] = relationship(
        back_populates="tasks"
    )

    def __repr__(self) -> str:
        return f"Task(task_id={self.task_id!r}, title={self.title!r}, is_completed={self.is_completed!r})"

