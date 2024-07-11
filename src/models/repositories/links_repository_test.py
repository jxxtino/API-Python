import pytest
import uuid
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="TEST PASS")
def test_create_links():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    links_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "link.com.br",
        "title": "Link Viagem"
    }
    links_repository.create_links(links_info)

@pytest.mark.skip(reason="TEST PASS")
def test_find_link_by_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    links = links_repository.find_link_by_trip(trip_id)
    print()
    print(links)