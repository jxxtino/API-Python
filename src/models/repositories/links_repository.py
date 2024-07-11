from sqlite3 import Connection
from typing import Dict, Tuple, List

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_links(self, links_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, link, trip_id, title)
                VALUES
                    (?,?,?,?)
            ''', (  
                links_infos["id"],
                links_infos["link"],
                links_infos["trip_id"],
                links_infos["title"],
            )
        )
        self.__conn.commit()

    def find_link_by_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM links WHERE trip_id = ?
            ''', (trip_id,)
        )
        links = cursor.fetchall()
        return links