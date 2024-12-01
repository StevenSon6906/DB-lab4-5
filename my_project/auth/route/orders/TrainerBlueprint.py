from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import trainers_controller
from my_project.auth.controller.orders.TrainersController import TrainersController
from my_project.auth.domain.orders.Trainer import Trainer

trainer_bp = Blueprint('trainer', __name__, url_prefix='/trainer')

@trainer_bp.get('/all')
def get_all_trainers_with_gender() -> Response:
    trainers = trainers_controller.find_with_gender()
    trainers_dto = [trainer.put_into_large_dto() for trainer in trainers]
    return make_response(jsonify(trainers_dto), HTTPStatus.OK)

@trainer_bp.get('')
def get_all_trainers() -> Response:
    trainers = trainers_controller.find_all()
    trainers_dto = [trainer.put_into_dto() for trainer in trainers]
    return make_response(jsonify(trainers_dto), HTTPStatus.OK)

@trainer_bp.post('')
def create_trainer() -> Response:
    content = request.get_json()
    trainer = Trainer.create_from_dto(content)
    trainers_controller.create(trainer)
    return make_response(jsonify(trainer.put_into_dto()), HTTPStatus.CREATED)

@trainer_bp.get('/<int:trainer_id>')
def get_trainer(trainer_id: int) -> Response:
    trainer = trainers_controller.find_by_id(trainer_id)
    if trainer:
        return make_response(jsonify(trainer.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Trainer not found"}), HTTPStatus.NOT_FOUND)

@trainer_bp.put('/<int:trainer_id>')
def update_trainer(trainer_id: int) -> Response:
    content = request.get_json()
    trainer = Trainer.create_from_dto(content)
    trainers_controller.update(trainer_id, trainer)
    return make_response("Trainer updated", HTTPStatus.OK)

@trainer_bp.delete('/<int:trainer_id>')
def delete_trainer(trainer_id: int) -> Response:
    trainers_controller.delete(trainer_id)
    return make_response("Trainer deleted", HTTPStatus.NO_CONTENT)