import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="criando emails")
def test_emails_to_invite():
    conn = db_connection_handler.get_connection()
    emails_to_invite = EmailsToInviteRepository(conn)

    emails_trip_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "matheus@email.com"
    }
    emails_to_invite.emails_to_invite(emails_trip_infos)

@pytest.mark.skip(reason="buscando emails")
def test_emails_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite = EmailsToInviteRepository(conn)    
    email = emails_to_invite.find_emails_from_trip(trip_id)
    print()
    print(email) 