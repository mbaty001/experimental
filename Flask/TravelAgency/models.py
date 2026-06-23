from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


# Define the base class for declarative models
class Base(DeclarativeBase):
    pass


# Define the Client model
class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    phone: Mapped[str | None] = mapped_column(String, nullable=True)
    address: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    # Define a relationship to the Itinerary model
    itineraries: Mapped[list["Itinerary"]] = relationship(
        "Itinerary", back_populates="client", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, name={self.name!r}, email={self.email!r})"


# Define the Itinerary model
class Itinerary(Base):
    __tablename__ = "itineraries"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    destination: Mapped[str] = mapped_column(String, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    activities: Mapped[str | None] = mapped_column(String, nullable=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        onupdate=datetime.now(timezone.utc),
    )

    # Define a relationship to the Client model
    client: Mapped[Client] = relationship("Client", back_populates="itineraries")

    def __repr__(self) -> str:
        return f"Itinerary(id={self.id!r}, destination={self.destination!r}, start_date={self.start_date!r}, end_date={self.end_date!r})"
