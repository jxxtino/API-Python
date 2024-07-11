from     sqlite3 import Connection
from typing import Dict, Tuple, List

class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_email(self, emails_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO emails_to_invite
                    (id, trip_id, email)
                VALUES
                    (?,?,?)
            ''', (  
                emails_infos["id"],
                emails_infos["trip_id"],
                emails_infos["email"]
            )
        )
        self.__conn.commit()

    def find_emails_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(''' SELECT * FROM emails_to_invite WHERE trip_id = ? ''', (trip_id,))
        emails = cursor.fetchall()
        return emails
