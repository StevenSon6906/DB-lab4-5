from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import programs_controller
from my_project.auth.domain.orders.Program import Program

program_bp = Blueprint('program', __name__, url_prefix='/program')

@program_bp.get('')
def get_all_programs() -> Response:
    programs = programs_controller.find_all()
    programs_dto = [program.put_into_dto() for program in programs]
    return make_response(jsonify(programs_dto), HTTPStatus.OK)

@program_bp.post('')
def create_program() -> Response:
    content = request.get_json()
    program = Program.create_from_dto(content)
    programs_controller.create(program)
    return make_response(jsonify(program.put_into_dto()), HTTPStatus.CREATED)

@program_bp.get('/<int:program_id>')
def get_program(program_id: int) -> Response:
    program = programs_controller.find_by_id(program_id)
    if program:
        return make_response(jsonify(program.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Program not found"}), HTTPStatus.NOT_FOUND)

@program_bp.put('/<int:program_id>')
def update_program(program_id: int) -> Response:
    content = request.get_json()
    program = Program.create_from_dto(content)
    programs_controller.update(program_id, program)
    return make_response("Program updated", HTTPStatus.OK)

@program_bp.delete('/<int:program_id>')
def delete_program(program_id: int) -> Response:
    programs_controller.delete(program_id)
    return make_response("Program deleted", HTTPStatus.NO_CONTENT)