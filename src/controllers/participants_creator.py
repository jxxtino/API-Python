import uuid
from typing import Dict

class ParticipantCreator():
    def __init__(self, participant_repository, emails_to_invite_repository) -> None:
        self.participant_repository = participant_repository
        self.emails_to_invite_repository = emails_to_invite_repository

    def create(self, body, trip_id) -> Dict:
        try:
            participant_id = str(uuid.uuid4())
            email_id = str(uuid.uuid4())

            emails_info = {
                "id": email_id,
                "trip_id": trip_id,
                "email": body["email"],
            }

            participant_info = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"]
            }

            self.participant_repository.create_participants(participant_info)
            self.emails_to_invite_repository.registry_email(emails_info)

            return {
                "body": {"participant_id": participant_id},
                "status_code": 201
            }

        except Exception as exeception:
            return{
                "body": {"error": "Bad Request", "message": str(exeception)},
                "status_code": 400
            }