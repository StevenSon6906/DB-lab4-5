from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import program_exercises_controller
from my_project.auth.domain.orders.ProgramExercise import ProgramExercise

program_exercise_bp = Blueprint('program_exercise', __name__, url_prefix='/program_exercise')

@program_exercise_bp.get('/all')
def get_all_program_exercises_and_related_data() -> Response:
    exercises = program_exercises_controller.find_all_with_related_data()
    exercises_dto = [exercise.put_into_large_dto() for exercise in exercises]
    return make_response(jsonify(exercises_dto), HTTPStatus.OK)

@program_exercise_bp.get('')
def get_all_program_exercises() -> Response:
    program_exercises = program_exercises_controller.find_all()
    program_exercises_dto = [program_exercise.put_into_large_dto() for program_exercise in program_exercises]
    return make_response(jsonify(program_exercises_dto), HTTPStatus.OK)

@program_exercise_bp.post('')
def create_program_exercise() -> Response:
    content = request.get_json()
    program_exercise = ProgramExercise.create_from_dto(content)
    program_exercises_controller.create(program_exercise)
    return make_response(jsonify(program_exercise.put_into_dto()), HTTPStatus.CREATED)

@program_exercise_bp.get('/<int:program_exercise_id>')
def get_program_exercise(program_exercise_id: int) -> Response:
    program_exercise = program_exercises_controller.find_by_id(program_exercise_id)
    if program_exercise:
        return make_response(jsonify(program_exercise.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Program Exercise not found"}), HTTPStatus.NOT_FOUND)

@program_exercise_bp.put('/<int:program_exercise_id>')
def update_program_exercise(program_exercise_id: int) -> Response:
    content = request.get_json()
    program_exercise = ProgramExercise.create_from_dto(content)
    program_exercises_controller.update(program_exercise_id, program_exercise)
    return make_response("Program Exercise updated", HTTPStatus.OK)

@program_exercise_bp.delete('/<int:program_exercise_id>')
def delete_program_exercise(program_exercise_id: int) -> Response:
    program_exercises_controller.delete(program_exercise_id)
    return make_response("Program Exercise deleted", HTTPStatus.NO_CONTENT)