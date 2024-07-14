from flask import jsonify,Blueprint, request

# Controller
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer

from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

from src.controllers.participants_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.participant_confirmer import ParticipantConfirmer

from src.controllers.activities_creator import ActivityCreator
from src.controllers.activity_finder import ActivityFinder


# Repos
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository 
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

# Conn
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    
    controller = TripCreator(trips_repository,emails_repository)
    response = controller.create(request.json)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    controller = TripConfirmer(trips_repository)
    response = controller.confirm(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    controller = TripFinder(trips_repository)
    response = controller.find_trip_details(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/create", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    controller = LinkCreator(links_repository)
    response = controller.confirm(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    controller = LinkFinder(links_repository)
    response = controller.find(tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invite", methods=["POST"])
def invite_to_trip(tripId):
    conn = db_connection_handler.get_connection()
    parcipants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)

    controller = ParticipantCreator(parcipants_repository, emails_repository)
    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/participants", methods=["GET"])
def find_participant_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    controller = ParticipantFinder(participant_repository)
    response = controller.find_participants_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/participant/<participantId>/confirm", methods=["PATCH"])
def confirm_participant_for_trip(participantId):
    conn = db_connection_handler.get_connection()
    participant_repository = ParticipantsRepository(conn)

    controller = ParticipantConfirmer(participant_repository)
    response = controller.confirm(participantId)

    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activity", methods=["POST"])
def create_trip_activity(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityCreator(activity_repository)
    response = controller.create(request.json, tripId)

    return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activity", methods=["GET"])
def find_activity_from_trip(tripId):
    conn = db_connection_handler.get_connection()
    activity_repository = ActivitiesRepository(conn)

    controller = ActivityFinder(activity_repository)
    response = controller.find_activity_from_trip(tripId)

    return jsonify(response["body"]), response["status_code"]