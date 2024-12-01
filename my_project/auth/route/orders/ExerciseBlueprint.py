from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import exercises_controller
from my_project.auth.domain.orders.Exercise import Exercise

exercise_bp = Blueprint('exercise', __name__, url_prefix='/exercise')

@exercise_bp.get('')
def get_all_exercises() -> Response:
    exercises = exercises_controller.find_all()
    exercises_dto = [exercise.put_into_dto() for exercise in exercises]
    return make_response(jsonify(exercises_dto), HTTPStatus.OK)

@exercise_bp.post('')
def create_exercise() -> Response:
    content = request.get_json()
    exercise = Exercise.create_from_dto(content)
    exercises_controller.create(exercise)
    return make_response(jsonify(exercise.put_into_dto()), HTTPStatus.CREATED)

@exercise_bp.get('/<int:exercise_id>')
def get_exercise(exercise_id: int) -> Response:
    exercise = exercises_controller.find_by_id(exercise_id)
    if exercise:
        return make_response(jsonify(exercise.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Exercise not found"}), HTTPStatus.NOT_FOUND)

@exercise_bp.put('/<int:exercise_id>')
def update_exercise(exercise_id: int) -> Response:
    content = request.get_json()
    exercise = Exercise.create_from_dto(content)
    exercises_controller.update(exercise_id, exercise)
    return make_response("Exercise updated", HTTPStatus.OK)

@exercise_bp.delete('/<int:exercise_id>')
def delete_exercise(exercise_id: int) -> Response:
    exercises_controller.delete(exercise_id)
    return make_response("Exercise deleted", HTTPStatus.NO_CONTENT)