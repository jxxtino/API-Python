from     sqlite3 import Connection
from typing import Dict, Tuple, List

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activitie(self, activitie_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO activities
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?,?,?,?)
            ''', (  
                activitie_infos["id"],
                activitie_infos["trip_id"],
                activitie_infos["title"],
                activitie_infos["occurs_at"],
            )
        )
        self.__conn.commit()

    def find_activitie_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            ''' 
                SELECT * FROM activities WHERE trip_id = ? 
            ''', (trip_id,))
        
        activitie = cursor.fetchall()
        return activitie
