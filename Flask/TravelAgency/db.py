from sqlalchemy import select, update, delete
from app_init import db
from models import Client, Itinerary
from datetime import datetime

# Client operations
def create_client(name: str, email: str, phone: str|None = None, address: str|None = None) -> Client:
    new_client = Client(name=name, email=email, phone=phone, address=address)
    db.session.add(new_client)
    db.session.commit()
    return new_client

def get_client(client_id: int) -> Client|None:
    return db.session.get(Client, client_id)

def list_clients() -> list[Client]:
    return db.session.execute(select(Client)).scalars().all()

def update_client(client_id: int, name: str|None = None, email: str|None = None, phone: str|None = None, address: str|None = None) -> Client|None:
    client = db.session.get(Client, client_id)
    if not client:
        return None
    if name is not None:
        client.name = name
    if email is not None:
        client.email = email
    if phone is not None:
        client.phone = phone
    if address is not None:
        client.address = address
    db.session.commit()
    return client

def delete_client(client_id: int) -> bool:
    client = db.session.get(Client, client_id)
    if not client:
        return None
    db.session.delete(client)
    db.session.commit()
    return client

def create_itinerary(client_id: int, destination: str, start_date: datetime, end_date: datetime, activities: str|None = None) -> Itinerary:
    client = db.session.get(Client, client_id)
    if not client:
        raise ValueError(f"Client not found. Id: {client_id}")
    new_itinerary = Itinerary(destination=destination, start_date=start_date, end_date=end_date, activities=activities, client=client)
    db.session.add(new_itinerary)
    db.session.commit()
    return new_itinerary

def get_itinerary(itinerary_id: int) -> Itinerary|None:
    return db.session.get(Itinerary, itinerary_id)

def list_itineraries() -> list[Itinerary]:
    return db.session.execute(select(Itinerary)).scalars().all()

def update_itinerary(itinerary_id: int, destination: str|None = None, start_date: datetime|None = None, end_date: datetime|None = None, activities: str|None = None) -> Itinerary|None:
    itinerary = db.session.get(Itinerary, itinerary_id)
    if not itinerary:
        return None
    if destination is not None:
        itinerary.destination = destination
    if start_date is not None:
        itinerary.start_date = start_date
    if end_date is not None:
        itinerary.end_date = end_date
    if activities is not None:
        itinerary.activities = activities
    db.session.commit()
    return itinerary

def delete_itinerary(itinerary_id: int) -> bool:
    itinerary = db.session.get(Itinerary, itinerary_id)
    if not itinerary:
        return False
    db.session.delete(itinerary)
    db.session.commit()
    return True