from typing import Dict
import uuid

class LinkCreator():
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def confirm(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())    
            links_infos = {
                "link": body["url"],
                "title": body["title"],
                "link_id": link_id,
                "trip_id": trip_id
            }

            self.__links_repository.registry_links(links_infos)

            return{
                "body": { "link_Id": link_id },
                "status_code": 201
            }
        
        except Exception as exeception:
            return{
                "body": {"error": "Bad Request", "message": str(exeception)},
                "status_code": 400
            }