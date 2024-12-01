from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import trainer_visits_controller
from my_project.auth.domain.orders.TrainerVisit import TrainerVisit

trainer_visit_bp = Blueprint('trainer_visit', __name__, url_prefix='/trainer_visit')

@trainer_visit_bp.get('')
def get_all_trainer_visits() -> Response:
    visits = trainer_visits_controller.find_all()
    visits_dto = [visit.put_into_dto() for visit in visits]
    return make_response(jsonify(visits_dto), HTTPStatus.OK)

@trainer_visit_bp.post('')
def create_trainer_visit() -> Response:
    content = request.get_json()
    visit = TrainerVisit.create_from_dto(content)
    trainer_visits_controller.create(visit)
    return make_response(jsonify(visit.put_into_dto()), HTTPStatus.CREATED)

@trainer_visit_bp.get('/<int:visit_id>')
def get_trainer_visit(visit_id: int) -> Response:
    visit = trainer_visits_controller.find_by_id(visit_id)
    if visit:
        return make_response(jsonify(visit.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Trainer Visit not found"}), HTTPStatus.NOT_FOUND)

@trainer_visit_bp.put('/<int:visit_id>')
def update_trainer_visit(visit_id: int) -> Response:
    content = request.get_json()
    visit = TrainerVisit.create_from_dto(content)
    trainer_visits_controller.update(visit_id, visit)
    return make_response("Trainer Visit updated", HTTPStatus.OK)

@trainer_visit_bp.delete('/<int:visit_id>')
def delete_trainer_visit(visit_id: int) -> Response:
    trainer_visits_controller.delete(visit_id)
    return make_response("Trainer Visit deleted", HTTPStatus.NO_CONTENT)