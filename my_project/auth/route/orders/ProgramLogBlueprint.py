from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import programs_logs_controller
from my_project.auth.domain.orders.ProgramLog import ProgramLog

program_log_bp = Blueprint('program_log', __name__, url_prefix='/program_log')

@program_log_bp.get('')
def get_all_program_logs() -> Response:
    logs = programs_logs_controller.find_all()
    logs_dto = [log.put_into_dto() for log in logs]
    return make_response(jsonify(logs_dto), HTTPStatus.OK)

@program_log_bp.post('')
def create_program_log() -> Response:
    content = request.get_json()
    log = ProgramLog.create_from_dto(content)
    programs_logs_controller.create(log)
    return make_response(jsonify(log.put_into_dto()), HTTPStatus.CREATED)

@program_log_bp.get('/<int:log_id>')
def get_program_log(log_id: int) -> Response:
    log = programs_logs_controller.find_by_id(log_id)
    if log:
        return make_response(jsonify(log.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Program Log not found"}), HTTPStatus.NOT_FOUND)

@program_log_bp.put('/<int:log_id>')
def update_program_log(log_id: int) -> Response:
    content = request.get_json()
    log = ProgramLog.create_from_dto(content)
    programs_logs_controller.update(log_id, log)
    return make_response("Program Log updated", HTTPStatus.OK)

@program_log_bp.delete('/<int:log_id>')
def delete_program_log(log_id: int) -> Response:
    programs_logs_controller.delete(log_id)
    return make_response("Program Log deleted", HTTPStatus.NO_CONTENT)