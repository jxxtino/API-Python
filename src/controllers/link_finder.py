class LinkFinder():
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def find(self, tripId) -> None:
        try:
            links = self.__links_repository.find_link_by_trip(tripId)

            formatted_links = []

            for link in links:
                formatted_links.append({
                    "id": link[0],
                    "url": link[2],
                    "title": link[3]
                })

            return {
                "body": {"links": formatted_links},
                "status_code": 200
            }

        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }

