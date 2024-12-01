from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import programs_timetable_controller
from my_project.auth.domain.orders.ProgramTimetable import ProgramTimetable

program_timetable_bp = Blueprint('program_timetable', __name__, url_prefix='/program_timetable')

@program_timetable_bp.get('')
def get_all_program_timetables() -> Response:
    timetables = programs_timetable_controller.find_all()
    timetables_dto = [timetable.put_into_dto() for timetable in timetables]
    return make_response(jsonify(timetables_dto), HTTPStatus.OK)

@program_timetable_bp.post('')
def create_program_timetable() -> Response:
    content = request.get_json()
    timetable = ProgramTimetable.create_from_dto(content)
    programs_timetable_controller.create(timetable)
    return make_response(jsonify(timetable.put_into_dto()), HTTPStatus.CREATED)

@program_timetable_bp.get('/<int:timetable_id>')
def get_program_timetable(timetable_id: int) -> Response:
    timetable = programs_timetable_controller.find_by_id(timetable_id)
    if timetable:
        return make_response(jsonify(timetable.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Program Timetable not found"}), HTTPStatus.NOT_FOUND)

@program_timetable_bp.put('/<int:timetable_id>')
def update_program_timetable(timetable_id: int) -> Response:
    content = request.get_json()
    timetable = ProgramTimetable.create_from_dto(content)
    programs_timetable_controller.update(timetable_id, timetable)
    return make_response("Program Timetable updated", HTTPStatus.OK)

@program_timetable_bp.delete('/<int:timetable_id>')
def delete_program_timetable(timetable_id: int) -> Response:
    programs_timetable_controller.delete(timetable_id)
    return make_response("Program Timetable deleted", HTTPStatus.NO_CONTENT)