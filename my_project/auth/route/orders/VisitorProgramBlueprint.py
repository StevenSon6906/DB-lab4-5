from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import visitor_programs_controller
from my_project.auth.domain.orders.VisitorProgram import VisitorProgram

visitor_program_bp = Blueprint('visitor_program', __name__, url_prefix='/visitor_program')

@visitor_program_bp.get('')
def get_all_visitor_programs() -> Response:
    visitor_programs = visitor_programs_controller.find_all()
    visitor_programs_dto = [visitor_program.put_into_dto() for visitor_program in visitor_programs]
    return make_response(jsonify(visitor_programs_dto), HTTPStatus.OK)

@visitor_program_bp.post('')
def create_visitor_program() -> Response:
    content = request.get_json()
    visitor_program = VisitorProgram.create_from_dto(content)
    visitor_programs_controller.create(visitor_program)
    return make_response(jsonify(visitor_program.put_into_dto()), HTTPStatus.CREATED)

@visitor_program_bp.get('/<int:visitor_program_id>')
def get_visitor_program(visitor_program_id: int) -> Response:
    visitor_program = visitor_programs_controller.find_by_id(visitor_program_id)
    if visitor_program:
        return make_response(jsonify(visitor_program.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Visitor Program not found"}), HTTPStatus.NOT_FOUND)

@visitor_program_bp.put('/<int:visitor_program_id>')
def update_visitor_program(visitor_program_id: int) -> Response:
    content = request.get_json()
    visitor_program = VisitorProgram.create_from_dto(content)
    visitor_programs_controller.update(visitor_program_id, visitor_program)
    return make_response("Visitor Program updated", HTTPStatus.OK)

@visitor_program_bp.delete('/<int:visitor_program_id>')
def delete_visitor_program(visitor_program_id: int) -> Response:
    visitor_programs_controller.delete(visitor_program_id)
    return make_response("Visitor Program deleted", HTTPStatus.NO_CONTENT)